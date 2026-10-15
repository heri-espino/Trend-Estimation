@echo off
setlocal
cd /d "%~dp0"
if not exist "build" mkdir "build"

where latexmk >nul 2>&1
if errorlevel 1 (
    echo Missing latexmk. Install MiKTeX or TeX Live and ensure latexmk is on PATH.
    exit /b 1
)

latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build slides.tex
if errorlevel 1 (
    echo Presentation compilation failed. See build\slides.log for details.
    exit /b 1
)
copy /Y "build\slides.pdf" "Numerical_Methods_Presentation.pdf" >nul
if errorlevel 1 exit /b 1
echo.
echo Compiled presentation: "%CD%\Numerical_Methods_Presentation.pdf"
echo.
echo If any figures still show placeholders, generate them with:
echo python "working_papers/Working Paper - Numerical Methods/presentation/build_figures.py" --group all
exit /b 0
