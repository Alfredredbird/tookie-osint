#!/usr/bin/env bash
set -e

PROJECT_NAME="tookie-osint"
BIN_PATH="/usr/local/bin/$PROJECT_NAME"

OS="$(uname -s)"
case "$OS" in
    Linux*)  INSTALL_DIR="/opt/$PROJECT_NAME" ;;
    Darwin*) INSTALL_DIR="/usr/local/opt/$PROJECT_NAME" ;;
    *) echo "Unsupported OS"; exit 1 ;;
esac

if [[ "$EUID" -ne 0 ]]; then
    echo "Run with sudo"
    exit 1
fi

rm -f "$BIN_PATH"
rm -rf "$INSTALL_DIR"

echo "[✓] Uninstalled $PROJECT_NAME"