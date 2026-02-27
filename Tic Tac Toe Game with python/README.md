# 🎮 Tic Tac Toe Game using Python (Tkinter)

A simple **GUI-based Tic Tac Toe game** built using Python and Tkinter.
This project demonstrates basic GUI development, event handling, and game logic implementation in Python.

---

## 📌 Project Overview

This is a 2-player Tic Tac Toe game where:

* Player **X** and Player **O** take turns
* The game checks for a winner after every move
* The winning combination is highlighted in **green**
* A popup message displays the winner

This project is perfect for beginners learning:

* Python GUI development
* Tkinter library
* Game logic implementation
* Event-driven programming

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** (Built-in Python GUI library)
* **MessageBox** from tkinter

---

## 🚀 How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed.

Check version:

```bash
python --version
```

### Step 2: Save the File

Save your code as:

```bash
Tic_Tac_Toe_Game_with_python.py
```

### Step 3: Run the Program

```bash
python Tic_Tac_Toe_Game_with_python.py
```

The game window will open.

---

## 🎯 Game Features

✅ 3x3 grid layout
✅ Player turn display
✅ Winner detection logic
✅ Winning cells highlighted
✅ Popup message for winner

---

## 🧠 How the Game Works

### 1️⃣ Game Board

* Created using 9 Tkinter buttons
* Stored in a list called `buttons`

### 2️⃣ Player Turns

* Starts with Player **X**
* Automatically switches after each move

```python
current_player = 'X'
```

### 3️⃣ Winner Logic

The function `check_winner()` checks all possible winning combinations:

* Rows
* Columns
* Diagonals

If a match is found:

* Buttons turn green
* Winner popup appears

---

## 📂 Project Structure

```
Tic-Tac-Toe/
│
├── Tic_Tac_Toe_Game_with_python.py
└── README.md
```

---

## 🎓 Concepts Covered

* Functions in Python
* Lists and indexing
* Lambda functions
* Tkinter Grid layout
* Event handling
* Conditional statements
* Basic game development logic

---

## 🔮 Future Improvements

You can enhance this project by adding:

* 🔁 Restart Game button
* 🤖 Single Player mode (AI)
* 🎨 Better UI styling
* 🟡 Draw match detection
* 🏆 Scoreboard system


