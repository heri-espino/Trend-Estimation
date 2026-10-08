# Backward-compatible Windows alias. Now preparation ONLY; never compiles LaTeX.
# Prefer paper_smoothness-cv/prepare-paper.ps1.
param(
    [switch]$SkipInstall,
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"
Write-Warning "build-workflow-paper.ps1 is now preparation-only; compile on macOS using compile-paper.sh."
& (Join-Path $PSScriptRoot "prepare-paper.ps1") @PSBoundParameters
