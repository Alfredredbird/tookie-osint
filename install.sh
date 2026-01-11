#!/usr/bin/env bash
set -e

# -------- CONFIG --------
PROJECT_NAME="tookie-osint"
SOURCE_DIR="$(pwd)"
PYTHON_BIN="python3"
# ------------------------

# Detect OS
OS="$(uname -s)"
IS_ALPINE=false

if [ -f /etc/alpine-release ]; then
    IS_ALPINE=true
fi

case "$OS" in
    Darwin*)
        INSTALL_DIR="/usr/local/opt/$PROJECT_NAME"
        BIN_PATH="/usr/local/bin/$PROJECT_NAME"
        CHOWN_CMD="chown -R root:wheel"
        ;;
    Linux*)
        if $IS_ALPINE; then
            INSTALL_DIR="/opt/$PROJECT_NAME"
            BIN_PATH="/usr/local/bin/$PROJECT_NAME"
            CHOWN_CMD="chown -R root:root"
        else
            INSTALL_DIR="/opt/$PROJECT_NAME"
            BIN_PATH="/usr/local/bin/$PROJECT_NAME"
            CHOWN_CMD="chown -R root:root"
        fi
        ;;
    *)
        echo "[!] Unsupported OS: $OS"
        exit 1
        ;;
esac

echo "[*] Installing $PROJECT_NAME"
echo "[*] OS: $OS"
$IS_ALPINE && echo "[*] Alpine / iSH detected"
echo "[*] Install dir: $INSTALL_DIR"

# Root check (skip on iSH since user is root)
if [ "$EUID" -ne 0 ] && ! $IS_ALPINE; then
    echo "[!] Please run as root (sudo)"
    exit 1
fi

# Remove existing install
if [ -d "$INSTALL_DIR" ]; then
    echo "[*] Removing existing install"
    rm -rf "$INSTALL_DIR"
fi

# Copy project files
echo "[*] Copying files..."
mkdir -p "$(dirname "$INSTALL_DIR")"
cp -r "$SOURCE_DIR" "$INSTALL_DIR"

# Create virtual environment
VENV_DIR="$INSTALL_DIR/.venv"
echo "[*] Creating virtual environment..."


if $IS_ALPINE; then
    if ! $PYTHON_BIN -m venv --help >/dev/null 2>&1; then
        echo
        echo "[!] Missing Python dependencies on Alpine / iSH"
        echo "Run this first:"
        echo
        echo "apk add --no-cache python3 py3-pip py3-virtualenv git"
        echo
        exit 1
    fi
    $PYTHON_BIN -m venv "$VENV_DIR"
else
    $PYTHON_BIN -m venv "$VENV_DIR"
fi

"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r "$INSTALL_DIR/requirements.txt"

# Create launcher
echo "[*] Writing launcher to $BIN_PATH"
cat << EOF > "$BIN_PATH"
#!/usr/bin/env sh
SCRIPT_DIR="$INSTALL_DIR"
VENV_DIR="\$SCRIPT_DIR/.venv"

if [ ! -d "\$VENV_DIR" ]; then
    echo "[!] Virtual environment missing. Reinstall required."
    exit 1
fi

exec "\$VENV_DIR/bin/python" "\$SCRIPT_DIR/brib.py" "\$@"
EOF

chmod +x "$BIN_PATH"

# Permissions
$CHOWN_CMD "$INSTALL_DIR" || true

echo "[✓] Installation complete!"
echo "Run with: $PROJECT_NAME"
