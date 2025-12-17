# 🚗 Quick Repair — ER:LC

Quick Repair is a real-time automation tool for Emergency Response: Liberty County (ER:LC) that automatically clicks Repair Car first, then Exit Garage, at high speed and in the correct order.

https://github.com/user-attachments/assets/43757c21-89aa-470c-813e-5283634cbcb1

---

## 📦 Requirements

- Windows
- Python 3.9 or newer
- Emergency Response: Liberty County running in windowed or borderless mode

---

## 🐍 Installing Python

1. Go to https://www.python.org/downloads/
2. Download Python 3.9 or newer
3. Make sure to check "Add Python to PATH" during installation
4. Complete the installation

Verify Python is installed:
```bash
python --version
```

---

## 📚 Install Required Libraries

Open Command Prompt in the project folder and run:
```bash
pip install opencv-python numpy mss pydirectinput
```

---

## 🖼️ Button Templates

You must provide the following image files in the same folder as the script:

- repair_button.png
- exit_garage_button.png

These should be tightly cropped screenshots of the buttons taken in-game at the same resolution you play on.

---

## ▶️ How to Run

1. Launch Emergency Response: Liberty County
2. Open the garage menu
3. Open Command Prompt in the project folder
4. Run:
```bash
python quick_repair.py
```

The script will continuously detect and click the buttons in real time.

Press Ctrl + C to stop the script.

---

## ⚠️ Disclaimer

This project is for educational and personal automation purposes only.  
You are responsible for how you use this tool.

---

## 🏁 Why Quick Repair?

Because clicking Repair then Exit hundreds of times is not fun.  
Automation is faster.

