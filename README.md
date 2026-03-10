# 🧠 AI Fitness Trainer – Real-Time Push-Up Counter with Voice Assistant

An **AI-powered fitness trainer application** built using **Python, Computer Vision, and Voice Interaction**.
The system can **count push-ups using a webcam**, **answer fitness questions through a chatbot**, and **interact using voice commands**. It also tracks workouts and generates **progress reports**.

This project demonstrates the integration of **AI concepts, GUI development, speech processing, and computer vision** into a single smart fitness application.

---

# 🚀 Features

### 🏋️ Real-Time Push-Up Counter

* Detects and counts push-ups using a webcam.
* Displays live workout data.
* Automatically stops when the workout ends.

### 🤖 AI Fitness Chatbot

* Built without external APIs.
* Answers questions related to:

  * Diet
  * Muscles
  * Workouts
  * Cardio
  * Fitness motivation
  * Recovery and rest

### 🎤 Voice Interaction

* Accepts **voice input** using speech recognition.
* Responds with **voice output** using text-to-speech.
* All chatbot responses appear in **text + audio**.

### 📊 Workout Progress Tracker

* Stores workout history in **CSV format**.
* Allows users to **save data using their own name**.
* Generates **progress reports and visual graphs**.

### 🖥️ Interactive GUI

* Built using **Tkinter**.
* Modern interface for:

  * Chat interaction
  * Workout start/stop
  * Progress visualization
  * Voice input

---

# 🛠️ Technologies Used

| Technology        | Purpose                      |
| ----------------- | ---------------------------- |
| Python            | Core programming language    |
| OpenCV            | Webcam and push-up detection |
| Tkinter           | Graphical User Interface     |
| SpeechRecognition | Voice input                  |
| pyttsx3           | Voice output                 |
| Pandas            | Data storage and analysis    |
| Matplotlib        | Progress graphs              |
| NumPy             | Numerical processing         |

---

# 📂 Project Structure

```
AI-Fitness-Trainer
│
├── gui.py                # Main GUI application
├── chat_bot.py           # AI fitness chatbot logic
├── voice_input.py        # Speech recognition
├── voice_output.py       # Text-to-speech system
├── pushup_counter.py     # Computer vision push-up detection
├── workout_tracker.py    # Workout data storage and progress tracking
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/AI-Fitness-Trainer.git
```

### 2️⃣ Navigate to Project Folder

```
cd AI-Fitness-Trainer
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the GUI application:

```
python gui.py
```

The interface will open where you can:

* Start push-up tracking
* Ask the chatbot fitness questions
* Use voice commands
* View workout progress

---

# 💬 Example Commands for Chatbot

You can ask questions like:

```
Hello
Start workout
Diet tips
How to build muscle
Best cardio exercises
Motivation
Show progress
```

---

# 📈 Progress Tracking

The system allows users to:

* Save workout data as **CSV**
* Track **push-up history**
* Visualize performance using **graphs**

Example data stored:

```
Date,Pushups
2026-03-10,15
2026-03-11,20
2026-03-12,25
```

---

# 🧠 How the System Works

1. The **webcam captures video frames**.
2. Computer vision analyzes movement to detect push-ups.
3. The **chatbot processes fitness questions** using rule-based logic.
4. Speech recognition converts **voice to text**.
5. Text-to-speech converts **AI responses into audio**.
6. Workout data is stored and visualized for progress tracking.

---

# 🔮 Future Improvements

* Pose detection for **more accurate exercise tracking**
* Support for **multiple exercises (squats, planks, etc.)**
* Mobile or web-based interface
* Personalized workout recommendations
* AI posture correction

---

# 👨‍💻 Author

**Prathmesh Yadav Patil**

Computer Science Student | Python Developer | AI Enthusiast

---

# ⭐ If You Like This Project

Give it a **star on GitHub** and feel free to contribute!

---
