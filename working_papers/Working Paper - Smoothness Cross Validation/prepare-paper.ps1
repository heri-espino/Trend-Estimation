# Windows preflight for the independent pooled forecast-CV manuscript; never compiles LaTeX.
param([switch]$SkipInstall, [switch]$SkipTests)
$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
function Invoke-PythonStep {
    param([string]$Label, [string[]]$Arguments)
    Write-Host "=== $Label ==="
    & python @Arguments
    if ($LASTEXITCODE -ne 0) { throw "$Label failed with exit code $LASTEXITCODE." }
}
Push-Location $root
try {
    if (-not $SkipInstall) {
        Invoke-PythonStep "Install editable package" @("-m","pip","install","-e",".")
    }
    if (-not $SkipTests) {
        Invoke-PythonStep "Run CV manuscript tests" @(
            "-m","pytest","-q",
            "tests/test_smoothness_plain_article.py",
            "tests/test_paper_platform_workflows.py",
            "tests/test_pooled_forecast_cv_lab.py"
        )
    }
    Invoke-PythonStep "Check manuscript and frozen CP03 figures" @(
        (Join-Path $PSScriptRoot "build.py"), "--check"
    )
    Write-Host 'Preparation complete. Compile on a LaTeX machine using compile-paper.sh.'
    git status --short
} finally { Pop-Location }
