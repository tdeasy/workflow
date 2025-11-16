#!/bin/bash
# n8n Installation Script

echo "🎵 House Music MIDI Generator - n8n Setup"
echo "=========================================="
echo ""

# Check if n8n is already installed
if command -v n8n &> /dev/null; then
    echo "✓ n8n is already installed!"
    n8n --version
    echo ""
    echo "To start n8n, run: n8n start"
    exit 0
fi

echo "Installing n8n..."
echo ""

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed!"
    echo "Please install Node.js first: https://nodejs.org/"
    exit 1
fi

echo "✓ Node.js version: $(node --version)"
echo ""

# Install n8n globally
echo "Installing n8n globally with npm..."
npm install -g n8n

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ n8n installed successfully!"
    echo ""
    echo "To start n8n:"
    echo "  n8n start"
    echo ""
    echo "Then open: http://localhost:5678"
    echo ""
    echo "To import workflows:"
    echo "  1. Open n8n web interface"
    echo "  2. Go to Workflows"
    echo "  3. Click 'Import from File'"
    echo "  4. Select: workflows/house-music-master.json"
else
    echo ""
    echo "❌ Installation failed!"
    echo "Try running with sudo: sudo npm install -g n8n"
fi
