import tkinter as tk
from tkinter import scrolledtext
import threading

from voice_input import listen
from voice_output import speak
from chat_bot import get_response
from pushup_counter import start_pushup_counter
from workout_tracker import save_workout, show_progress


# ---------------- WINDOW ---------------- #

window = tk.Tk()
window.title("AI Fitness Trainer")
window.geometry("720x650")
window.configure(bg="#0f172a")


# ---------------- TITLE ---------------- #

title = tk.Label(
    window,
    text="AI FITNESS TRAINER",
    font=("Segoe UI", 22, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=15)


# ---------------- CHAT AREA ---------------- #

chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg="#1e293b",
    fg="white",
    height=20,
    width=70
)

chat_area.pack(padx=20, pady=10)
chat_area.config(state="disabled")


def display(sender, message):

    chat_area.config(state="normal")

    if sender == "You":
        chat_area.insert(tk.END, f"\nYou: {message}\n", "user")

    else:
        chat_area.insert(tk.END, f"AI: {message}\n", "ai")

    chat_area.config(state="disabled")
    chat_area.yview(tk.END)


chat_area.tag_config("user", foreground="#22c55e")
chat_area.tag_config("ai", foreground="#38bdf8")


# ---------------- WORKOUT ---------------- #

def start_workout():

    display("AI", "Starting pushup workout")
    speak("Starting pushup workout")

    pushups = start_pushup_counter()

    save_workout(pushups)

    display("AI", f"You completed {pushups} pushups")
    speak(f"You completed {pushups} pushups")


# ---------------- TEXT MESSAGE ---------------- #

def send_message():

    text = entry.get()

    entry.delete(0, tk.END)

    if text == "":
        return

    display("You", text)

    if "start workout" in text or "pushup" in text:

        threading.Thread(target=start_workout).start()
        return

    if "progress" in text:

        show_progress()
        return

    answer = get_response(text)

    display("AI", answer)

    speak(answer)


# ---------------- VOICE COMMAND ---------------- #

def voice_command():

    display("AI", "Listening...")
    speak("I am listening")

    text = listen()

    if text == "":
        display("AI", "Sorry I didn't understand")
        speak("Sorry I didn't understand")
        return

    display("You", text)

    if "start workout" in text:

        threading.Thread(target=start_workout).start()
        return

    if "progress" in text:

        show_progress()
        return

    answer = get_response(text)

    display("AI", answer)

    speak(answer)


# ---------------- INPUT FIELD ---------------- #

entry = tk.Entry(
    window,
    font=("Segoe UI", 12),
    width=45,
    bg="#1e293b",
    fg="white",
    insertbackground="white"
)

entry.pack(pady=10)


# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(window, bg="#0f172a")
button_frame.pack()


send_btn = tk.Button(
    button_frame,
    text="Send",
    width=12,
    bg="#38bdf8",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    command=send_message
)

send_btn.grid(row=0, column=0, padx=5)


workout_btn = tk.Button(
    button_frame,
    text="Start Workout",
    width=14,
    bg="#22c55e",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    command=lambda: threading.Thread(target=start_workout).start()
)

workout_btn.grid(row=0, column=1, padx=5)


progress_btn = tk.Button(
    button_frame,
    text="Progress",
    width=12,
    bg="#f59e0b",
    fg="black",
    font=("Segoe UI", 10, "bold"),
    command=show_progress
)

progress_btn.grid(row=0, column=2, padx=5)


voice_btn = tk.Button(
    button_frame,
    text="🎤 Voice",
    width=12,
    bg="#ef4444",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=lambda: threading.Thread(target=voice_command).start()
)

voice_btn.grid(row=0, column=3, padx=5)


# ---------------- START MESSAGE ---------------- #

display("AI", "Hello! I am your AI fitness trainer.")
speak("Hello! I am your AI fitness trainer.")


window.mainloop()