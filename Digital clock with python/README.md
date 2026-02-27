# ⏰ Digital Clock using Python (Tkinter)

A simple and beautiful **Digital Clock GUI Application** built using Python and Tkinter.
The clock displays the current system time and updates every second automatically.

---

## 🎯 Project Overview

This project demonstrates how to build a real-time GUI application using:

* Python
* Tkinter (GUI library)
* time module

The clock updates continuously using Tkinter’s `after()` method.

---

## 🖥️ Output Preview

The application window:

* Displays current time in **HH:MM:SS format**
* Updates automatically every 200 milliseconds
* Uses large bold font for better visibility
* Custom background and text colors

Example:

```
14:35:08
```

---

## 🧠 How It Works

1. `Tk()` creates the main window.
2. `Label()` is used to display the time.
3. `time.strftime("%H:%M:%S")` fetches current system time.
4. `after(200, function)` updates the time every 200 milliseconds.
5. `mainloop()` keeps the window running.

---

## 📂 Project Structure

```
Digital-Clock/
│── Digital_clock_with_python.py
│── README.md
```

---

## 💻 Source Code

```python
from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font = ("Boulder", 68, "bold")
background = "#F2e750"
foreground = "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=background, 
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
```

---

## ▶️ How to Run the Project

1. Install Python (3.x recommended)
2. Save the file as `Digital_clock_with_python.py`
3. Open terminal or command prompt
4. Run:

```
python digital_clock.py
```

---

## 🔄 Optional Improvements

You can enhance this project by:

* Adding **12-hour format (AM/PM)**
* Adding **Date display**
* Creating **Dark Mode UI**
* Making it **fullscreen**
* Adding custom fonts and styling

---

## 🎓 What You Learn From This Project

* GUI development using Tkinter
* Working with real-time updates
* Using `after()` function for scheduling
* Handling fonts and styling in Tkinter

---

## 📌 Author

Chintan Dabhi

