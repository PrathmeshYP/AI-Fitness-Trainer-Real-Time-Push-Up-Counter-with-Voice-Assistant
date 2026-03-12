import pyttsx3
import threading
import queue

speech_queue = queue.Queue()

engine = pyttsx3.init()
engine.setProperty("rate", 165)
engine.setProperty("volume", 1)


def speech_worker():
    while True:
        text = speech_queue.get()
        if text is None:
            break

        engine.say(text)
        engine.runAndWait()


thread = threading.Thread(target=speech_worker, daemon=True)
thread.start()


def speak(text):
    speech_queue.put(text)