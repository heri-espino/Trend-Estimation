@echo off
setlocal

cd /d "%~dp0"
set "OUTPUT_NAME=EspinoMontelongo-2026-Statistical_Properties_of_Penalized_Trend_Estimators"

if not exist "build" mkdir "build"

latexmk -pdf -bibfudge- -auxdir="build" -outdir="%CD%" -jobname="%OUTPUT_NAME%" -interaction=nonstopmode -file-line-error "main.tex"
if errorlevel 1 goto :error

echo.
echo Paper compiled successfully: "%CD%\%OUTPUT_NAME%.pdf"
exit /b 0

:error
echo.
echo Paper compilation failed. Review the messages above.
pause
exit /b 1
