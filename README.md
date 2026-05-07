# Jarvis

Double-clap your hands and your Mac wakes up — Spotify plays, apps launch, and a voice greets you.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/Lemon-stack/jarvis/main/install.sh | bash
```

Requires macOS and Python 3.9+. Installs as a background service that starts on login.

## Configure

Edit `~/.jarvis/config.json`:

```json
{
  "voice": "Daniel",
  "apps": ["Spotify", "Arc", "Notion"]
}
```

| Key | Description |
|-----|-------------|
| `voice` | macOS voice name. Run `say -v '?'` to list installed voices. |
| `apps` | Apps to open. Spotify always opens first. |

## Logs

```bash
tail -f /tmp/jarvis.log
```

## Uninstall

```bash
launchctl unload ~/Library/LaunchAgents/com.jarvis.clap.plist
rm ~/Library/LaunchAgents/com.jarvis.clap.plist
pip3 uninstall jarvis
```
