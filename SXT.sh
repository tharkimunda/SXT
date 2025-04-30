#!/bin/bash

ARCH=$(uname -m)

if [[ "$ARCH" == "x86_64" ]]; then
    echo "64-bit system detected."
    chmod 777 SXT64
    ./SXT64
elif [[ "$ARCH" == "i386" || "$ARCH" == "i686" ]]; then
    echo "32-bit system detected."
    chmod 777 SXT
    ./SXT
else
    echo "Unknown architecture: $ARCH"
    exit 1
fi
