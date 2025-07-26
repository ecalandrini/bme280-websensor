#!/bin/bash

# Exit if any command fails
set -e

# Get absolute path of current directory
WORKING_DIR="$(cd "$(dirname "$0")" && pwd)"

# Service name
SERVICE_NAME="bme280-websensor"

# Template file (in repo)
TEMPLATE_FILE="$WORKING_DIR/${SERVICE_NAME}.service.template"

# Target systemd service file
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"

echo "📍 Working directory: $WORKING_DIR"
echo "🛠 Installing systemd service..."

# Replace placeholder with actual working directory
sed "s|{{WORKING_DIR}}|$WORKING_DIR|g" "$TEMPLATE_FILE" | sudo tee "$SERVICE_FILE" > /dev/null

# Reload systemd
sudo systemctl daemon-reload

# Enable and start the service
sudo systemctl enable "$SERVICE_NAME"
sudo systemctl start "$SERVICE_NAME"

echo "✅ Service '$SERVICE_NAME' installed and started!"
sudo systemctl status "$SERVICE_NAME" --no-pager
