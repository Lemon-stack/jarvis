import json
from pathlib import Path

CONFIG_DIR = Path.home() / "Documents" / "Jarvis"
CONFIG_PATH = CONFIG_DIR / "config.json"

DEFAULTS = {
    "apps": ["Spotify"],
    "voice": "Daniel",
}

def load():
    if not CONFIG_PATH.exists():
        CONFIG_DIR.mkdir(exist_ok=True)
        CONFIG_PATH.write_text(json.dumps(DEFAULTS, indent=2))
        print(f"Config created at {CONFIG_PATH} — edit it to customise.")
    with open(CONFIG_PATH) as f:
        data = json.load(f)
    return {**DEFAULTS, **data}
