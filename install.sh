#!/bin/bash
set -e

REPO="https://github.com/Lemon-stack/jarvis"  # update before sharing

echo "Installing Jarvis..."

if ! command -v python3 &>/dev/null; then
    echo "Python 3 not found."
    echo "Download and install it from https://python.org, then run this script again."
    exit 1
fi

TMP=$(mktemp -d)
curl -fsSL "$REPO/archive/refs/heads/main.tar.gz" | tar -xz -C "$TMP" --strip-components=1
pip3 install "$TMP" --quiet

PYTHON_BIN="$(python3 -m site --user-base)/bin"
if [[ ":$PATH:" != *":$PYTHON_BIN:"* ]]; then
    echo "export PATH=\"$PYTHON_BIN:\$PATH\"" >> "$HOME/.zshrc"
    export PATH="$PYTHON_BIN:$PATH"
fi

JARVIS_BIN=$(command -v jarvis)

PLIST="$HOME/Library/LaunchAgents/com.jarvis.clap.plist"
mkdir -p "$HOME/Library/LaunchAgents"

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.jarvis.clap</string>
    <key>ProgramArguments</key>
    <array>
        <string>$JARVIS_BIN</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/jarvis.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/jarvis.log</string>
</dict>
</plist>
EOF

launchctl load "$PLIST"

# trigger config file creation then open it
jarvis &
JARVIS_PID=$!
sleep 2
kill $JARVIS_PID 2>/dev/null

open -a TextEdit "$HOME/.jarvis/config.json"

echo ""
echo "Jarvis installed and running. It will start automatically on every login."
echo "Your config file has opened in TextEdit — add your Spotify URI and apps, then save."
