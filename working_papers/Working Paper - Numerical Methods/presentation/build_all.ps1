# Run from anywhere in PowerShell, with the trend-estimation Python environment active.
# Generates the 28 presentation figures from frozen results; then compiles slides.tex.
# It does not rerun the Monte Carlo experiments or modify results/.
$ErrorActionPreference = "Stop"
$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Repo = (Resolve-Path (Join-Path $Here "..\..\..")).Path

Write-Host "[1/2] Rendering all presentation figures as vector PDF..."
Push-Location $Repo
try {
    & python (Join-Path $Here "build_figures.py") --group all --format pdf
    if ($LASTEXITCODE -ne 0) { throw "Figure builder failed (exit code $LASTEXITCODE)." }
}
finally {
    Pop-Location
}

Write-Host "[2/2] Compiling widescreen LaTeX presentation..."
Push-Location $Here
try {
    if (-not (Get-Command latexmk -ErrorAction SilentlyContinue)) {
        throw "latexmk is not installed. Install MiKTeX or TeX Live with latexmk."
    }
    New-Item -Path "build" -ItemType Directory -Force | Out-Null
    & latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build slides.tex
    if ($LASTEXITCODE -ne 0) { throw "LaTeX build failed. See build/slides.log." }
    Copy-Item "build/slides.pdf" "Numerical_Methods_Presentation.pdf" -Force
    Write-Host "Presentation ready: $Here\Numerical_Methods_Presentation.pdf"
}
finally {
    Pop-Location
}
