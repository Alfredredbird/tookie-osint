# System variables

VERSION="1.0"
PKG="tookie-osint_${VERSION}_all"

mkdir -p $PKG/DEBIAN
mkdir -p $PKG/usr/bin
mkdir -p $PKG/usr/lib/tookie-osint

# Build
dpkg-deb --root-owner-group --build "$PKG"

OR 
run the script