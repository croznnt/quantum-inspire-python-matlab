[CmdletBinding()]
param(
    [ValidateSet('core', 'research', 'platform', 'all')]
    [string]$Group = 'core',
    [switch]$ListOnly
)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
$sourceRoot = Join-Path $projectRoot 'sources'
$catalog = Import-Csv -LiteralPath (Join-Path $projectRoot 'catalog/repositories.csv')
$selected = @($catalog | Where-Object {
    $priority = $_.priority
    switch ($Group) {
        'core' { $priority -eq 'core' }
        'research' { $priority -in @('core', 'extended') }
        'platform' { $priority -eq 'platform' }
        'all' { $priority -ne 'historical' }
    }
})
if ($ListOnly) {
    $selected | Select-Object repository, language, category
    return
}
foreach ($entry in $selected) {
    if ($entry.repository -notmatch '^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$') {
        throw "Invalid repository: $($entry.repository)"
    }
    $parts = $entry.repository.Split('/')
    if ($parts -contains '.' -or $parts -contains '..') {
        throw "Invalid repository path: $($entry.repository)"
    }
    $ownerRoot = Join-Path $sourceRoot $parts[0]
    $destination = Join-Path $ownerRoot $parts[1]
    if (Test-Path -LiteralPath $destination) {
        Write-Host "Skip existing path: $destination"
        continue
    }
    New-Item -ItemType Directory -Force -Path $ownerRoot | Out-Null
    & git clone "https://github.com/$($entry.repository).git" $destination
    if ($LASTEXITCODE -ne 0) { throw "Clone failed: $($entry.repository)" }
}
