#!/bin/bash
set -e

VERSION=$(cat config/version | tr -d '[:space:]' | sed 's/^v//')
PKG="tookie-osint_${VERSION}_all"

echo "[*] Building $PKG.deb..."

# Clean previous build entirely
rm -rf "$PKG" "$PKG.deb"

# Create structure
mkdir -p "$PKG/DEBIAN"
mkdir -p "$PKG/usr/bin"
mkdir -p "$PKG/usr/lib/tookie-osint"

# Copy source files
cp brib.py "$PKG/usr/lib/tookie-osint/"
cp -r config modules sites lang "$PKG/usr/lib/tookie-osint/"

# Clean up compiled Python files
find "$PKG/usr/lib/tookie-osint" -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find "$PKG/usr/lib/tookie-osint" -name "*.pyc" -delete 2>/dev/null || true

# Verify files actually got copied
echo "[*] Files in package lib dir:"
ls "$PKG/usr/lib/tookie-osint/"

# Launcher
cat > "$PKG/usr/bin/tookie-osint" << 'EOF'
#!/bin/bash
exec python3 /usr/lib/tookie-osint/brib.py "$@"
EOF
chmod 755 "$PKG/usr/bin/tookie-osint"

# control
cat > "$PKG/DEBIAN/control" << EOF
Package: tookie-osint
Version: $VERSION
Architecture: all
Maintainer: Alfredredbird
Depends: python3, python3-requests, chromium-driver
Description: Username OSINT scanner
 Scan websites for a given username across many platforms.
EOF

# postinst
cat > "$PKG/DEBIAN/postinst" << 'EOF'
#!/bin/bash
set -e
pip3 install --break-system-packages --ignore-installed selenium webdriver-manager python-dotenv
chmod +x /usr/bin/tookie-osint
echo "[+] tookie-osint installed!"
EOF
chmod 755 "$PKG/DEBIAN/postinst"

# prerm
cat > "$PKG/DEBIAN/prerm" << 'EOF'
#!/bin/bash
set -e
echo "[*] Removing tookie-osint..."
EOF
chmod 755 "$PKG/DEBIAN/prerm"

# Build
dpkg-deb --root-owner-group --build "$PKG"
echo "[+] Done: $PKG.deb"