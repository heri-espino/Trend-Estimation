@echo off
setlocal

cd /d "%~dp0"

python build.py
if errorlevel 1 (
    echo.
    echo Paper compilation failed. Review the messages above.
    pause
    exit /b 1
)

echo.
echo Paper compiled successfully: "%CD%\EspinoMontelongo-2026-Forecast_Optimal_Smoothness.pdf"
