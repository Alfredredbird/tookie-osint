#!/usr/bin/env bash
set -e

# -------- CONFIG --------
PROJECT_NAME="tookie-osint"
SOURCE_DIR="$(pwd)"
BIN_PATH="/usr/local/bin/$PROJECT_NAME"
PYTHON_BIN="python3"
# ------------------------

# Detect OS
OS="$(uname -s)"
case "$OS" in
    Linux*)
        INSTALL_DIR="/opt/$PROJECT_NAME"
        CHOWN_CMD="chown -R root:root"
        ;;
    Darwin*)
        INSTALL_DIR="/usr/local/opt/$PROJECT_NAME"
        CHOWN_CMD="chown -R root:wheel"
        ;;
    *)
        echo "[!] Unsupported OS: $OS"
        exit 1
        ;;
esac

echo "[*] Installing $PROJECT_NAME on $OS"
echo "[*] Install dir: $INSTALL_DIR"

# Ensure running as root
if [[ "$EUID" -ne 0 ]]; then
    echo "[!] Please run as root (sudo)"
    exit 1
fi

# Remove existing install
if [[ -d "$INSTALL_DIR" ]]; then
    echo "[*] Removing existing install"
    rm -rf "$INSTALL_DIR"
fi

# Copy project files
echo "[*] Copying files to $INSTALL_DIR..."
mkdir -p "$(dirname "$INSTALL_DIR")"
cp -r "$SOURCE_DIR" "$INSTALL_DIR"

# Create virtual environment
VENV_DIR="$INSTALL_DIR/.venv"
echo "[*] Creating virtual environment in $VENV_DIR..."
$PYTHON_BIN -m venv "$VENV_DIR"
"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r "$INSTALL_DIR/requirements.txt"

# Create launcher script
echo "[*] Writing launcher to $BIN_PATH"
cat << EOF > "$BIN_PATH"
#!/usr/bin/env bash
SCRIPT_DIR="$INSTALL_DIR"
VENV_DIR="\$SCRIPT_DIR/.venv"

# Ensure virtual environment exists
if [ ! -d "\$VENV_DIR" ]; then
    echo "[!] Virtual environment missing! Please reinstall."
    exit 1
fi

exec "\$VENV_DIR/bin/python" "\$SCRIPT_DIR/brib.py" "\$@"
EOF

chmod +x "$BIN_PATH"

# Fix permissions
$CHOWN_CMD "$INSTALL_DIR"

echo "[✓] Installation complete!"
echo "Run with: $PROJECT_NAME"
