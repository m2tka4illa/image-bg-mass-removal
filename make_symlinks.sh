#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

ln -s "$SCRIPT_DIR/input" ~/Desktop/bg-input
ln -s "$SCRIPT_DIR/output" ~/Desktop/bg-output

echo "Symlinks created on Desktop."
