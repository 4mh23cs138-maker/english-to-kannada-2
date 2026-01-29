@echo off
echo ========================================
echo English to Kannada Translator Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/4] Creating backend virtual environment...
cd backend
python -m venv venv
call venv\Scripts\activate.bat

echo [2/4] Installing Python dependencies...
pip install -r requirements.txt

echo [3/4] Backend setup complete!
echo.
echo [4/4] To start the application:
echo.
echo Terminal 1 - Start Backend:
echo   cd backend
echo   venv\Scripts\activate
echo   python app.py
echo.
echo Terminal 2 - Start Frontend:
echo   cd frontend
echo   python -m http.server 8000
echo.
echo Then open http://localhost:8000 in your browser
echo.
pause
