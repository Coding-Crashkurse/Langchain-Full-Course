@echo off

REM Upgrading pip
echo Installing pip
call python -m pip install pip --upgrade
echo Done

REM Creating virtual environment
echo Creating virtual environment
call python -m venv .venv
echo Done

REM Activating the virtual environment
echo Activating the virtual environment
call %CD%\.venv\Scripts\activate.bat
echo Done

REM Install the required packages from requirements.txt
echo Installing required packages from requirements.txt
call pip install -r requirements.txt
echo Done
