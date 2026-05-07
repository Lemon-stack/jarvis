import subprocess
import time
from datetime import datetime


def speak(text, voice):
    subprocess.run(['say', '-v', voice, text])


def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning, sir."
    elif hour < 17:
        return "Good afternoon, sir."
    else:
        return "Good evening, sir."


def open_apps(apps):
    for app in apps:
        subprocess.run(['open', '-a', app])


SPOTIFY_TRACK_URI = "spotify:track:1NyDtpaR99dby36DaA4ziL"


def play_spotify_track(uri=SPOTIFY_TRACK_URI):
    subprocess.Popen(['open', '-a', 'Spotify'])
    time.sleep(1)
    subprocess.run(['osascript', '-e', f'''
    tell application "Spotify"
        set sound volume to 0
        play track "{uri}"
    end tell
    '''])
    time.sleep(2)
    subprocess.run(['osascript', '-e', '''
    tell application "Spotify"
        set player position to 5
        set sound volume to 100
    end tell
    '''])


def trigger_jarvis(cfg, skip_spotify=False):
    import threading
    if not skip_spotify:
        threading.Thread(target=play_spotify_track, daemon=True).start()
    other_apps = [a for a in cfg['apps'] if a.lower() != 'spotify']
    if other_apps:
        def delayed_open(apps):
            time.sleep(4)
            open_apps(apps)
        threading.Thread(target=lambda: delayed_open(other_apps), daemon=True).start()
    speak(get_greeting(), cfg['voice'])
    time.sleep(0.4)
    speak("All systems nominal at the moment this time. Loading your environment.", cfg['voice'])
