import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".jarvis"
CONFIG_PATH = CONFIG_DIR / "config.json"

DEFAULTS = {
    "_help": {
        "apps": "List of Mac apps to open on trigger. Example: [\"Spotify\", \"Chrome\"]",
        "spotify_track_uri": "Right-click a song in Spotify > Share > Copy Song Link. Paste the URI here.",
        "voice": "Mac voice to use. Options: Daniel, Alex, Samantha, Karen, Moira"
    },
    "apps": ["Spotify"],
    "spotify_track_uri": "",
    "voice": "Daniel",
}

def load():
    if not CONFIG_PATH.exists():
        CONFIG_DIR.mkdir(exist_ok=True)
        CONFIG_PATH.write_text(json.dumps(DEFAULTS, indent=2))
    with open(CONFIG_PATH) as f:
        data = json.load(f)
    cfg = {**DEFAULTS, **data}
    cfg.pop("_help", None)
    return cfg
