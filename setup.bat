@echo off
REM Prepara el entorno virtual e instala las dependencias en Windows.
setlocal

cd /d "%~dp0"

where py >nul 2>&1
if %errorlevel%==0 (
    set PYTHON=py -3
) else (
    set PYTHON=python
)

if not exist ".venv" (
    echo Creando entorno virtual en .venv...
    %PYTHON% -m venv .venv
    if errorlevel 1 goto :error
)

echo Actualizando pip e instalando dependencias...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto :error

echo.
echo Listo. Inicia la aplicacion con:
echo     python runApp.py
goto :eof

:error
echo Ocurrio un error durante la instalacion. >&2
exit /b 1
