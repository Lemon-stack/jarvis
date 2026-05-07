import threading
import time
import numpy as np
from .actions import trigger_jarvis, play_spotify_track

last_clap_time = 0
first_clap_time = 0
clap_count = 0
jarvis_active = False


CLAP_THRESHOLD = 2.5
DOUBLE_CLAP_WINDOW = 0.7
MIN_CLAP_GAP = 0.2


def make_callback(cfg):
    threshold = CLAP_THRESHOLD
    window = DOUBLE_CLAP_WINDOW
    min_gap = MIN_CLAP_GAP

    def detect_clap(indata, frames, callback_time, status):
        global last_clap_time, first_clap_time, clap_count, jarvis_active
        if jarvis_active:
            return
        volume = np.linalg.norm(indata) * 10
        current_time = time.monotonic()

        if volume > threshold:
            if current_time - last_clap_time < min_gap:
                return
            last_clap_time = current_time

            if clap_count == 0:
                clap_count = 1
                first_clap_time = current_time
            elif current_time - first_clap_time <= window:
                clap_count = 0
                print("Double clap detected! Activating...")
                jarvis_active = True
                threading.Thread(target=play_spotify_track, daemon=True).start()
                threading.Thread(target=lambda: trigger_jarvis(cfg, skip_spotify=True), daemon=True).start()
            else:
                clap_count = 1
                first_clap_time = current_time

    return detect_clap
