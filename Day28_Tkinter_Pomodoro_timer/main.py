from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

BLUE = "#D1E9F6"
YELLOW = "#F6EACB"
BEIGE = "#F1D3CE"
PEACH = "#EECAD5"
FONT_NAME = "Arial"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""

# ---------------------------- COLOR CHANGE ------------------------------- #

def color_change(color):
    title_label.config(bg=color)
    window.config(bg=color)
    canvas.config(bg=color)
    checkmark.config(bg=color)

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    color_change(BEIGE)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0
    global marks
    marks = ""

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if reps == 8:
        countdown(8)
        title_label.config(text="Break 😎")
        color_change(BLUE)
    elif reps % 2 == 0:
        countdown(2)
        title_label.config(text="Break ☕")
        color_change(PEACH)
    elif reps % 2 != 0:
        countdown(4)
        title_label.config(text="Work 💻")
        color_change(YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        global marks
        marks = ""
        start_timer()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=BEIGE)

title_label = Label(text="Timer", bg=BEIGE, font=("Courier", 30, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

checkmark = Label(bg=BEIGE)
checkmark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30,"bold"))
canvas.grid(row=1, column=1)

window.mainloop()