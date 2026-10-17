@echo off
setlocal
set "SCRIPT=%~dp0bloomberg-practice.ps1"
where pwsh >nul 2>nul
if not errorlevel 1 goto :pwsh
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT%" %*
exit /b %errorlevel%
:pwsh
pwsh -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT%" %*
exit /b %errorlevel%
