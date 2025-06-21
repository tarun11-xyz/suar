
# 🤖🎙️ SUAR: Systematic User Assistant Robot – A Voice-Controlled Python Assistant

**SUAR (Systematic User Assistant Robot)** is a lightweight and beginner-friendly voice-controlled desktop assistant built in Python 🐍. It responds to the wake word **"suar"**, listens to your commands, and performs tasks like opening websites or playing music. This project is perfect for learning about voice recognition, speech synthesis, and Python automation.

---

## 🚀 Features

- 🗣️ Wake word detection – activates on **"suar"**
- 🎧 Voice recognition using Google Speech API
- 🗨️ Text-to-speech responses using `pyttsx3`
- 🌐 Web automation:
  - Google
  - YouTube
  - Facebook
  - GitHub
  - Instagram
- 🎶 Music playback using a custom `musicLib`
- ❌ Basic error handling for smoother performance
- 🔁 Continuous listening loop

---

## 🛠️ Installation

### 📦 Requirements

> Make sure Python 3.7+ is installed. Then, install the dependencies:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```
---

> ⚠️ If `pyaudio` fails to install on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## 📁 Project Structure

```
SUAR/
├── suar.py          # Main script
├── musicLib.py      # Dictionary of song names and YouTube links
└── README.md        # Project documentation
```

---

## ▶️ How to Run

```bash
python suar.py
```

Make sure your microphone 🎤 is connected and functional. The assistant will:

1. Greet you with a welcome message
2. Wait for the wake word **"suar"**
3. Listen for your command (e.g., "open google", "play despacito")
4. Perform the required action using web automation or music links

---

## 🧠 Example Commands

* `open google`
* `open youtube`
* `open github`
* `play despacito` (Assuming it's in `musicLib.py`)

---

## 📌 To-Do

* [ ] Add more dynamic command processing
* [ ] Integrate ChatGPT API for open-ended queries
* [ ] Add voice customization options
* [ ] GUI interface with Tkinter or PyQt

---

## 🤝 Contributing

Feel free to fork this repository, submit pull requests, or open issues for feature requests or bugs.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Author

Made with ❤️ by \Tarun

```

---

Let me know if you'd like me to generate `musicLib.py` or help publish the repo with tags and topics for better visibility.
```
