#!/bin/bash

echo "🔧 Installing dependencies for ComfyUI_LoadImageFromHttpURL..."

# Exit immediately on error
set -e

# Activate virtual environment if it exists
if [ -d "../../venv" ]; then
    echo "📦 Activating ComfyUI virtual environment..."
    source ../../venv/bin/activate
else
    echo "⚠️  No virtual environment found at ../../venv"
    echo "➡️  Continuing with system/global Python environment"
fi

# Install required packages
echo "📥 Installing from requirements.txt..."
pip install -r requirements.txt

echo "✅ Installation complete!"
