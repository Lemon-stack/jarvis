import time
import sounddevice as sd
from .config import load
from .actions import speak
from .detection import make_callback


def main():
    cfg = load()
    callback = make_callback(cfg)

    print("Jarvis is listening for double claps... (Ctrl+C to stop)")
    speak("All online.", cfg['voice'])

    try:
        with sd.InputStream(samplerate=44100, channels=1, callback=callback, blocksize=1024):
            while True:
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nJarvis shutting down.")
        speak("Goodbye, sir.", cfg['voice'])


if __name__ == "__main__":
    main()
