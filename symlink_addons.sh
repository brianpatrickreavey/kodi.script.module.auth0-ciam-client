#!/bin/bash

# Symlink script for Kodi addon development
# Usage: ./symlink_addons.sh --create | --remove

set -e

# Detect OS and set Kodi addons dir
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    KODI_DIR="$APPDATA/Kodi/addons"
else
    KODI_DIR="$HOME/.kodi/addons"
fi

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ADDON_DIR="$BASE_DIR/script.module.auth0-ciam-client"
HARNESS_DIR="$BASE_DIR/dev/script.auth0-ciam-client-test-harness"
ADDON_TARGET="$KODI_DIR/script.module.auth0-ciam-client"
HARNESS_TARGET="$KODI_DIR/script.auth0-ciam-client-test-harness"

create_symlinks() {
    mkdir -p "$KODI_DIR"
    if [ ! -L "$ADDON_TARGET" ]; then
        ln -s "$ADDON_DIR" "$ADDON_TARGET"
        echo "Symlinked main addon to $ADDON_TARGET"
    else
        echo "Main addon symlink already exists"
    fi
    if [ ! -L "$HARNESS_TARGET" ]; then
        ln -s "$HARNESS_DIR" "$HARNESS_TARGET"
        echo "Symlinked test harness to $HARNESS_TARGET"
    else
        echo "Test harness symlink already exists"
    fi
}

remove_symlinks() {
    if [ -L "$ADDON_TARGET" ]; then
        rm "$ADDON_TARGET"
        echo "Removed main addon symlink"
    else
        echo "No main addon symlink to remove"
    fi
    if [ -L "$HARNESS_TARGET" ]; then
        rm "$HARNESS_TARGET"
        echo "Removed test harness symlink"
    else
        echo "No test harness symlink to remove"
    fi
}

validate_symlinks() {
    if [ -L "$ADDON_TARGET" ]; then
        echo "Main addon symlink exists: $ADDON_TARGET -> $(readlink "$ADDON_TARGET")"
    else
        echo "Main addon symlink does not exist"
    fi
    if [ -L "$HARNESS_TARGET" ]; then
        echo "Test harness symlink exists: $HARNESS_TARGET -> $(readlink "$HARNESS_TARGET")"
    else
        echo "Test harness symlink does not exist"
    fi
}

case "$1" in
    --create)
        create_symlinks
        ;;
    --remove)
        remove_symlinks
        ;;
    --validate)
        validate_symlinks
        ;;
    *)
        echo "Usage: $0 --create | --remove | --validate"
        exit 1
        ;;
esac