#!/bin/bash

echo "========================================"
echo "English to Kannada Translator Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

echo "[1/4] Creating backend virtual environment..."
cd backend
python3 -m venv venv
source venv/bin/activate

echo "[2/4] Installing Python dependencies..."
pip install -r requirements.txt

echo "[3/4] Backend setup complete!"
echo ""
echo "[4/4] To start the application:"
echo ""
echo "Terminal 1 - Start Backend:"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python app.py"
echo ""
echo "Terminal 2 - Start Frontend:"
echo "  cd frontend"
echo "  python -m http.server 8000"
echo ""
echo "Then open http://localhost:8000 in your browser"
echo ""
