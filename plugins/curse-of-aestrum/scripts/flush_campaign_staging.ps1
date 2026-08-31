# flush_campaign_staging.ps1 — flush the active scene's staging file into the
# campaign's monolith overlays + the transcript, then delete staging.
#
# CoA analogue of Pandora's scripts/flush_staging.ps1. The shared *doctrine*
# (staging mechanism, transcript carve-out, save = flush) lives upstream in
# Calliope's scene_lifecycle.md (§5a-bis) and Aria's story_lifecycle.md
# ("Staging (work-scoped)"). This script is CoA's concrete flush: it APPENDS to
# the existing per-entity monolith overlays (CoA does NOT shard), in the exact
# byte format fiction-host writes (runtime/state.py::format_delta /
# append_delta) so a campaign played in either mode stays parse-compatible.
#
# Usage (any PowerShell host — pwsh 7+ on macOS/Linux/Windows, or Windows
# PowerShell 5.1 on Windows):
#   pwsh       -NoProfile -ExecutionPolicy Bypass -File scripts/flush_campaign_staging.ps1 -Campaign <campaign-id>
#   powershell -NoProfile -ExecutionPolicy Bypass -File scripts/flush_campaign_staging.ps1 -Campaign <campaign-id> -DryRun
#
# The scene skill invokes this via an OS-agnostic Bash one-liner that selects
# pwsh when present and falls back to Windows PowerShell — see
# overrides/scene.md "Save protocol — CoA specifics".
#
# Staging file format (campaign_state/<C>/staging/<sid>.md):
#   # Objective log                  -> append to timelines/saved/aestrum_events.md
#   # Experience deltas
#     ## party/<name>                -> append to party/saved/<name>.md
#     ## npcs/<name>                 -> append to npcs/saved/<name>.md
#   # Entity overlays
#     ## factions/<id>               -> append to factions/saved/<id>.md
#     ## items/<id>                  -> append to items/saved/<id>.md
#     ## locations/<id>              -> append to locations/saved/<id>.md
#   # Transcript                     -> write conversation_states/<sid>.md (verbatim)
# Each h2 (and the objective-log) body is a `### Day N - desc` block + bullets.

param(
    [Parameter(Mandatory=$true)]
    [string]$Campaign,

    [switch]$DryRun,

    [string]$RepoRoot
)

$ErrorActionPreference = 'Stop'

# Resolve the repo root in the *body*, not the param default. Under
# `powershell -File <relative-path>` (how the scene skill invokes this via
# Bash), $PSScriptRoot is empty at param-binding time but reliably set here.
if (-not $RepoRoot) {
    $scriptDir = $PSScriptRoot
    if (-not $scriptDir) { $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path }
    $RepoRoot = (Resolve-Path (Join-Path $scriptDir "..")).Path
}

# Write UTF-8 *without* a BOM, regardless of host. Windows PowerShell 5.1's
# `Set-Content -Encoding utf8` prepends a BOM; pwsh 7 does not. fiction-host
# writes overlays as UTF-8 no-BOM (state.py `path.write_text(..., encoding="utf-8")`),
# and this script APPENDS to those same files — so a BOM introduced mid-stream
# would corrupt the overlay. An explicit encoder keeps bytes identical across
# hosts and across the Claude-Code / fiction-host write paths.
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
function Write-Utf8NoBom {
    param([string]$Path, [string]$Text)
    [System.IO.File]::WriteAllText($Path, $Text, $Utf8NoBom)
}

# Append a delta block to a monolith overlay, creating it if absent. Mirrors
# fiction-host's runtime/state.py::append_delta (lines 277-288): the new block
# is separated from any prior content by exactly one blank line, and the file
# ends with a single trailing newline. CR/LF tolerant at the boundary so a
# mixed-ending file is not double-spaced.
function Append-Delta {
    param([string]$Path, [string]$Block)
    $existing = ''
    if (Test-Path $Path) { $existing = [System.IO.File]::ReadAllText($Path) }
    if ($existing) { $existing = $existing.TrimEnd("`r", "`n") + "`n`n" }
    $new = $existing + $Block.TrimEnd("`r", "`n") + "`n"
    if (-not $DryRun) {
        $dir = Split-Path -Parent $Path
        if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
        Write-Utf8NoBom -Path $Path -Text $new
        Write-Host "appended -> $Path"
    } else {
        Write-Host "[dry-run] would append -> $Path"
    }
}

$campaignRoot = Join-Path $RepoRoot "campaign_state/$Campaign"
if (-not (Test-Path $campaignRoot)) {
    throw "Campaign dir not found: $campaignRoot"
}

$stagingDir = Join-Path $campaignRoot "staging"
if (-not (Test-Path $stagingDir)) {
    throw "Staging dir not found: $stagingDir"
}

$stagingFiles = Get-ChildItem -Path $stagingDir -Filter '*.md' -File
if ($stagingFiles.Count -eq 0) {
    throw "No staging file found in $stagingDir"
}
if ($stagingFiles.Count -gt 1) {
    throw "Multiple staging files in $stagingDir - cannot flush ambiguously: $($stagingFiles.Name -join ', ')"
}

$stagingFile = $stagingFiles[0]
$sceneId = [System.IO.Path]::GetFileNameWithoutExtension($stagingFile.Name)
$content = Get-Content -Path $stagingFile.FullName -Raw -Encoding utf8

# Strip the YAML frontmatter (between two '---' lines at the top, optional).
$body = $content
if ($content -match '^(?s)---\s*\r?\n.*?\r?\n---\s*\r?\n(.*)$') {
    $body = $matches[1]
}

# Carve the Transcript off FIRST, before any section splitting. The transcript
# is the terminal freeform-prose region: everything from the `# Transcript` h1
# to EOF is the transcript, taken verbatim. It is NOT sub-split, so a prose line
# that happens to begin with `# ` (a read-aloud heading, a reproduced document,
# "# of bodies they never found:") can never be mistaken for a section boundary
# and silently truncate the save. (Calliope scene_lifecycle.md §5a-bis carve-out.)
$transcriptRegion = $null
$structuralBody = $body
$split = $body -split '(?m)^#[ \t]+Transcript[ \t]*\r?$', 2
if ($split.Count -eq 2) {
    $structuralBody = $split[0]
    $transcriptRegion = $split[1].Trim("`r", "`n", " ", "`t")
}

# Split the structural body into top-level sections on lines starting with
# '# ' (h1). Lookahead split preserves the header line with each section.
$sectionParts = $structuralBody -split "(?m)(?=^#\s)"
$sections = @{}
foreach ($part in $sectionParts) {
    if ([string]::IsNullOrWhiteSpace($part)) { continue }
    if ($part -match '(?s)^#\s+([^\r\n]+)\r?\n(.*)$') {
        $sectionName = $matches[1].Trim()
        $sectionBody = $matches[2].Trim("`r", "`n", " ", "`t")
        $sections[$sectionName] = $sectionBody
    }
}

if (-not $sections.ContainsKey('Experience deltas')) {
    throw "Staging file is missing required section: '# Experience deltas'"
}

# Split an h1 section body into `## <header>` sub-sections -> ordered list of
# @{ Header; Body }.
function Split-H2 {
    param([string]$Text)
    $out = @()
    foreach ($part in ($Text -split "(?m)(?=^##\s)")) {
        if ([string]::IsNullOrWhiteSpace($part)) { continue }
        if ($part -match '(?s)^##\s+([^\r\n]+)\r?\n(.*)$') {
            $out += [PSCustomObject]@{
                Header = $matches[1].Trim()
                Body   = $matches[2].Trim("`r", "`n", " ", "`t")
            }
        }
    }
    return ,$out
}

# Saved-overlay subdir per save-domain. The objective log and transcript are
# special-cased below.
$expDomains    = @('party', 'npcs')
$entityDomains = @('factions', 'items', 'locations')

# --- Objective log -> timelines/saved/aestrum_events.md ---------------------
if ($sections.ContainsKey('Objective log')) {
    $objBody = $sections['Objective log'].Trim("`r", "`n", " ", "`t")
    if ($objBody) {
        Append-Delta -Path (Join-Path $campaignRoot 'timelines/saved/aestrum_events.md') -Block $objBody
    }
}

# --- Experience deltas -> party/saved or npcs/saved ------------------------
foreach ($sub in (Split-H2 $sections['Experience deltas'])) {
    if ($sub.Header -notmatch '^([^/]+)/(.+)$') {
        throw "Experience delta sub-section header must be '<domain>/<name>' (domain in party|npcs): '$($sub.Header)'"
    }
    $domain = $matches[1]; $name = $matches[2]
    if ($expDomains -notcontains $domain) {
        throw "Experience delta domain must be one of [$($expDomains -join ', ')]: got '$domain' in '$($sub.Header)'"
    }
    Append-Delta -Path (Join-Path $campaignRoot "$domain/saved/$name.md") -Block $sub.Body
}

# --- Entity overlays -> factions/items/locations saved ---------------------
if ($sections.ContainsKey('Entity overlays')) {
    foreach ($sub in (Split-H2 $sections['Entity overlays'])) {
        if ($sub.Header -notmatch '^([^/]+)/(.+)$') {
            throw "Entity overlay sub-section header must be '<domain>/<id>': '$($sub.Header)'"
        }
        $domain = $matches[1]; $id = $matches[2]
        if ($entityDomains -notcontains $domain) {
            throw "Entity overlay domain must be one of [$($entityDomains -join ', ')]: got '$domain' in '$($sub.Header)'"
        }
        Append-Delta -Path (Join-Path $campaignRoot "$domain/saved/$id.md") -Block $sub.Body
    }
}

# --- Transcript -> conversation_states/<sid>.md (verbatim, overwrite) -------
if ($null -ne $transcriptRegion -and $transcriptRegion) {
    $txPath = Join-Path $campaignRoot "conversation_states/$sceneId.md"
    if (-not $DryRun) {
        $txDir = Split-Path -Parent $txPath
        if (-not (Test-Path $txDir)) { New-Item -ItemType Directory -Path $txDir -Force | Out-Null }
        Write-Utf8NoBom -Path $txPath -Text $transcriptRegion
        Write-Host "wrote -> $txPath"
    } else {
        Write-Host "[dry-run] would write -> $txPath"
    }
} else {
    Write-Host "[warn] no Transcript section in staging - skipping transcript write"
}

# --- Delete staging ---------------------------------------------------------
if (-not $DryRun) {
    Remove-Item -Path $stagingFile.FullName -Force
    Write-Host "deleted $($stagingFile.FullName)"
} else {
    Write-Host "[dry-run] would delete $($stagingFile.FullName)"
}

$mode = 'DONE'
if ($DryRun) { $mode = 'DRY RUN' }
Write-Host ""
Write-Host "$mode - scene $sceneId flushed for campaign $Campaign"
