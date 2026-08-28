@echo off
REM Simple helper to create a venv, install requirements, and run the Streamlit app
REM Requires Python to be installed and available on PATH
:: Check for python
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python not found on PATH. Please install Python and ensure "python" is available from the command line.
    pause
    exit /b 1
)
:: Create venv if it doesn't exist
if not exist .venv (
    python -m venv .venv
)
:: Activate venv
call .venv\Scripts\activate.bat
:: Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt
:: Run Streamlit app
streamlit run app.py
:: Keep window open after exit
pause
