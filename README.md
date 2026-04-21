# ⚡ Smart Thunder Vision — Hand Gesture Lightning Controller

A **Computer Vision Smart Project** where your **hand gestures control lightning strikes** in a storm image.

When you raise your fingers:

* ☝️ 1 finger → 1 lightning strike
* ✌️ 2 fingers → 2 lightning strikes
* 🖐️ 5 fingers → Full thunderstorm

The system uses **AI hand detection** to create a **real-time interactive thunder animation**.

---

# 🎯 Project Demo Idea

Black thunder sky image appears on screen:

* Raise **1 finger** → ⚡ One lightning strike
* Raise **2 fingers** → ⚡⚡ Two lightning strikes
* Raise **3 fingers** → ⚡⚡⚡ Three lightning strikes
* Raise **5 fingers** → 🌩️ Full thunderstorm

With:

* 🎥 Real-time camera detection
* ⚡ Lightning animation
* 🔊 Thunder sound effects
* 🎨 Storm visual effects

---

# 🧠 Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy
* Computer Vision
* Hand Gesture Recognition

---

# 📁 Project Structure

```
SmartThunder/
│
├── smart_thunder.py
├── lightning.png
├── thunder.jpg
├── thunder.mp3
├── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/smart-thunder.git
cd smart-thunder
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install mediapipe opencv-python numpy playsound
```

If you get NumPy error:

```bash
pip install "numpy<2"
```

---

# ▶️ Run Project

```bash
python smart_thunder.py
```

Camera will open and thunder animation starts ⚡

---

# 🎮 How To Use

| Fingers   | Action            |
| --------- | ----------------- |
| 1 Finger  | 1 Lightning       |
| 2 Fingers | 2 Lightning       |
| 3 Fingers | 3 Lightning       |
| 4 Fingers | 4 Lightning       |
| 5 Fingers | Full Thunderstorm |

---

# 🧠 How It Works

1. Camera detects your hand
2. MediaPipe identifies finger positions
3. Finger count detected
4. Lightning image displayed
5. Thunder sound plays
6. Animation triggered

---

# 🎥 Features

✅ Real-time hand tracking
✅ Lightning animation
✅ Thunder sound effects
✅ Interactive storm simulation
✅ Clean computer vision implementation

---

# 🚀 Future Improvements

* Add rain animation 🌧️
* Add lightning glow effect ⚡
* Add night sky animation 🌌
* Add gesture combinations
* Add AI weather simulator

---

# 💡 Use Cases

* Computer Vision Project
* AI Final Year Project
* Interactive Art Installation
* Smart Vision Demo
* AI + Animation Project

---

# 📸 Example

Show your hand:

🖐️

Storm appears:

⚡⚡⚡⚡⚡

---

# 👩‍💻 Author

Created by Hasni Maissa

---

# ⭐ If You Like This Project

Give it a star ⭐
Fork it 🍴
Improve it 🚀

---

# ⚡ Smart Thunder Vision

**Control the storm with your hands**
