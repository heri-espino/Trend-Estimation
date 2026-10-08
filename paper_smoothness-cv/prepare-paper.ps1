# Windows preparation ONLY. No LaTeX engine is invoked on this machine.
# From the repository root:
#   powershell -NoProfile -ExecutionPolicy Bypass -File .\paper_smoothness-cv\prepare-paper.ps1
param(
    [switch]$SkipInstall,
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$figures = Join-Path $PSScriptRoot "manuscript\figures"
$stem = "fig_workflow_tutorial"

function Invoke-PythonStep {
    param(
        [string]$Label,
        [string[]]$Arguments
    )
    Write-Host ""
    Write-Host "=== $Label ==="
    & python @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE."
    }
}

Push-Location $root
try {
    if (-not $SkipInstall) {
        Invoke-PythonStep -Label "Install editable Python package" -Arguments @(
            "-m", "pip", "install", "-e", "."
        )
    }

    if (-not $SkipTests) {
        Invoke-PythonStep -Label "Run manuscript and chronology tests" -Arguments @(
            "-m", "pytest", "-q",
            "tests/test_smoothness_workflow_tutorial.py",
            "tests/test_smoothness_plain_article.py"
        )
    }

    Invoke-PythonStep -Label "Regenerate tutorial figure and metadata" -Arguments @(
        "experiments/smoothness_cv/make_workflow_tutorial_figure.py"
    )

    foreach ($ext in @("pdf", "png", "json")) {
        $file = Join-Path $figures "$stem.$ext"
        if (-not (Test-Path -LiteralPath $file)) {
            throw "Missing generated figure artifact: $file"
        }
        if ((Get-Item -LiteralPath $file).Length -eq 0) {
            throw "Empty figure artifact: $file"
        }
    }

    # This is a source/figure preflight ONLY. --check does not run TeX.
    Invoke-PythonStep -Label "Validate manuscript source and figure references" -Arguments @(
        "paper_smoothness-cv/build.py", "--check"
    )

    Write-Host ""
    Write-Host "Windows preparation complete. NO LaTeX compilation was run."
    Write-Host "Review, commit and push manuscript/figures to GitHub."
    Write-Host "On macOS, pull and then run: bash paper_smoothness-cv/compile-paper.sh"
    git status --short
}
finally {
    Pop-Location
}
