@echo off
REM Ilham Command Launcher
REM Usage: Ilham filename.am

set args=%*
REM Remove any semicolon if typed
set args=%args:;=%

REM Run Python interpreter
python "%~dp0run_ilham.py" %args%
pause
