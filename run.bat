@echo off
REM Run Infrastructure Accessibility Tool (Windows)

echo.
echo ====================================================================== 
echo 🚀 INFRASTRUCTURE ACCESSIBILITY TOOL
echo ======================================================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
)

REM Activate virtual environment
echo.
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo 📥 Installing dependencies...
pip install -q -r requirements.txt
echo ✅ Dependencies installed

REM Run the main script
echo.
echo 🏃 Running analysis...
python main.py

echo.
echo 📂 Output files are in the 'output/' directory
echo ======================================================================
pause
