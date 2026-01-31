#!/usr/bin/env bash
set -e

PROJECT_NAME="tookie-osint"

OS="$(uname -s)"
IS_TERMUX=false

if [[ -n "$PREFIX" && "$PREFIX" == *"com.termux"* ]]; then
    IS_TERMUX=true
fi

case "$OS" in
    Linux*)
        if $IS_TERMUX; then
            INSTALL_DIR="$PREFIX/opt/$PROJECT_NAME"
            BIN_PATH="$PREFIX/bin/$PROJECT_NAME"
        else
            INSTALL_DIR="/opt/$PROJECT_NAME"
            BIN_PATH="/usr/local/bin/$PROJECT_NAME"
        fi
        ;;
    Darwin*)
        INSTALL_DIR="/usr/local/opt/$PROJECT_NAME"
        BIN_PATH="/usr/local/bin/$PROJECT_NAME"
        ;;
    *)
        echo "[!] Unsupported OS"
        exit 1
        ;;
esac

echo "[*] Uninstalling $PROJECT_NAME"
echo "[*] Install dir: $INSTALL_DIR"

# Root check (skip on Termux)
if [ "$EUID" -ne 0 ] && ! $IS_TERMUX; then
    echo "[!] Run with sudo"
    exit 1
fi

rm -f "$BIN_PATH"
rm -rf "$INSTALL_DIR"

echo "[✓] Uninstalled $PROJECT_NAME"