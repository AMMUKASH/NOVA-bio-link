#!/bin/bash
# Example cronjob script for VPS/Render
# Run bot restart every day at midnight

echo "Restarting NovaBot..."
pkill -f "python main.py"
nohup python main.py &
