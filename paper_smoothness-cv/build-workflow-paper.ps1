# Build the five-panel workflow tutorial and the Wiley manuscript.
# Run from anywhere with:
#   powershell -ExecutionPolicy Bypass -File .\paper_smoothness-cv\build-workflow-paper.ps1
param(
    [switch]$SkipTests
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$pdf = Join-Path $PSScriptRoot "EspinoMontelongo-2026-Forecast_Optimal_Smoothness.pdf"
$figure = Join-Path $PSScriptRoot "manuscript\figures\fig_workflow_tutorial.pdf"

function Invoke-PythonStep {
    param(
        [string]$Label,
        [string[]]$Arguments
    )
    Write-Host "=== $Label ==="
    & python @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed (exit code $LASTEXITCODE). No commit should be made."
    }
}

Push-Location $repoRoot
try {
    if (-not $SkipTests) {
        Invoke-PythonStep -Label "Workflow chronology tests" -Arguments @(
            "-m", "pytest", "-q", "tests/test_smoothness_workflow_tutorial.py"
        )
    }

    Invoke-PythonStep -Label "Generate five-panel tutorial" -Arguments @(
        "experiments/smoothness_cv/make_workflow_tutorial_figure.py"
    )

    if (-not (Test-Path -LiteralPath $figure)) {
        throw "The tutorial PDF was not generated: $figure"
    }

    $figureTime = (Get-Item -LiteralPath $figure).LastWriteTimeUtc

    Invoke-PythonStep -Label "Check Wiley manuscript" -Arguments @(
        "paper_smoothness-cv/build.py", "--check"
    )
    Invoke-PythonStep -Label "Compile Wiley manuscript" -Arguments @(
        "paper_smoothness-cv/build.py"
    )

    if (-not (Test-Path -LiteralPath $pdf)) {
        throw "The manuscript PDF was not generated: $pdf"
    }
    $pdfItem = Get-Item -LiteralPath $pdf
    if ($pdfItem.Length -lt 10000) {
        throw "The compiled PDF is unexpectedly small: $($pdfItem.Length) bytes."
    }
    if ($pdfItem.LastWriteTimeUtc -lt $figureTime) {
        throw "The compiled PDF predates the workflow figure. Build is stale."
    }

    Write-Host ""
    Write-Host "Build successful: $pdf"
    Write-Host "Figure: $figure"
    Write-Host "Review the PDF, then commit the generated figure and manuscript PDF."
    git status --short
}
finally {
    Pop-Location
}
