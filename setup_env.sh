#!/bin/bash
# Setup script for cluster environment

echo "Setting up environment..."

# Load Python module
module load python/3.9

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt --break-system-packages

# Create necessary directories
mkdir -p logs results

echo "Setup complete!"
echo "Virtual environment activated."