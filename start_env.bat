@echo off
setlocal

rem --- RUTA a Cmder.exe (ajústala si cambia) ---
set "CMDER=C:\Users\AsusTUF\Documents\Software\Cmder\Cmder.exe"

rem --- Carpeta del proyecto (la actual) ---
set "PROJ=%CD%"

rem --- Script de activación del venv ---
set "VENV=%PROJ%\venv\Scripts\activate.bat"

rem 1) Abrir la carpeta actual en VS Code (no bloquea)
start "" code "%PROJ%"

rem 2) Abrir Cmder aquí; si existe el venv, activarlo automáticamente
if exist "%VENV%" (
    start "" "%CMDER%" /start "%PROJ%" /x "-run cmd /k call ""%VENV%"""
) else (
    start "" "%CMDER%" /start "%PROJ%"
    echo [AVISO] No encontré "%VENV%".
)

endlocal
