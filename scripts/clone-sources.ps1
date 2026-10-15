[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$sourceRoot = Join-Path (Split-Path $PSScriptRoot -Parent) 'sources'
New-Item -ItemType Directory -Force -Path $sourceRoot | Out-Null
$repos = @(
    'quantuminspire',
    'qiskit-quantuminspire',
    'pennylane-quantuminspire',
    'quantum-inspire-examples',
    'OpenSquirrel',
    'libqasm',
    'OpenQL',
    'QuIS',
    'qilib'
)
foreach ($repo in $repos) {
    $destination = Join-Path $sourceRoot $repo
    if (Test-Path -LiteralPath $destination) {
        Write-Host "Skip existing path: $destination"
        continue
    }
    & git clone "https://github.com/QuTech-Delft/$repo.git" $destination
    if ($LASTEXITCODE -ne 0) {
        throw "Clone failed: $repo"
    }
}
