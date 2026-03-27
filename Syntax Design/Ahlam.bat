@echo off
REM Ahlam Command Launcher
REM Usage: Ahlam filename.am

set args=%*
REM Remove any semicolon if typed
set args=%args:;=%

REM Run Python interpreter
python "%~dp0run_ahlam.py" %args%
pause