# 🪨📄✂️ Rock Paper Scissor Game (Python)

A simple **Rock, Paper, Scissor** game built using Python.
The user plays against the computer, and the winner is decided based on classic game rules.

---

## 🎯 Project Overview

This is a beginner-friendly Python project that:

* Takes user input (Rock, Paper, or Scissor)
* Randomly generates computer choice
* Compares both choices
* Displays the winner
* Handles tie situations

---

## 🧠 How It Works

1️⃣ The program stores possible moves in a list:

```python
item_list = ['Rock','Paper','Scissor']
```

2️⃣ The user enters their move.

3️⃣ The computer randomly selects a move using Python’s built-in random module.

4️⃣ The program compares choices using conditional statements (`if-elif-else`).

5️⃣ The winner is displayed based on game rules:

* Rock beats Scissor
* Paper beats Rock
* Scissor beats Paper
* Same choices → Tie

---

## 💻 Technologies Used

* Python 3
* `random` module

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/Chintan1545/rock-paper-scissor.git
```

### Step 2: Navigate to Project Folder

```bash
cd rock-paper-scissor
```

### Step 3: Run the Python File

```bash
python Rock_Paper_Scissor_Game_with_python.py
```

---

## 📌 Sample Outputs

### ✅ Example 1

```
Enter your move = Rock,Paper,Scissor: Rock
User choice = Rock and computer choice = Scissor
Rock smashes Scissor: -> You win
```

### 🤝 Example 2

```
Enter your move = Rock,Paper,Scissor: Paper
User choice = Paper and computer choice = Paper
Both choose same: -> Match Tie
```

### ❌ Example 3

```
Enter your move = Rock,Paper,Scissor: Scissor
User choice = Scissor and computer choice = Rock
Rock smashes Scissor: -> Computer win
```

---

## 📂 Project Structure

```
rock-paper-scissor/
│
├── Rock_Paper_Scissor_Game_with_python.py
└── README.md
```

---

## 🚀 Future Improvements

* Add input validation (handle lowercase inputs)
* Add score tracking system
* Add multiple rounds
* Add GUI version using Tkinter
* Convert into a web version using Flask

---

## 🎓 What I Learned

* Working with Python lists
* Using the `random` module
* Writing conditional logic
* Handling user input
* Building small interactive CLI games

---

## 👨‍💻 Author

**Chintan Dabhi**
MCA Student | Python & AI Enthusiast