#!/bin/bash
# Run Infrastructure Accessibility Tool

echo ""
echo "======================================================================"
echo "🚀 INFRASTRUCTURE ACCESSIBILITY TOOL"
echo "======================================================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate || . venv/Scripts/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt
echo "✅ Dependencies installed"

# Run the main script
echo ""
echo "🏃 Running analysis..."
python main.py

echo ""
echo "📂 Output files are in the 'output/' directory"
echo "======================================================================"
