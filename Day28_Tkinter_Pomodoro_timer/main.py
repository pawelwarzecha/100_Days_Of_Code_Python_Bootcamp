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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    countdown(602)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")

    if count > 0:
        window.after(1000, countdown, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=BEIGE)

title_label = Label(text="Timer", bg=BEIGE, font=("Courier", 30, "bold"))
title_label.grid(row=0, column=1)

start_button = Button(text="Start",command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

checkmark = Label(text="✅")

canvas = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30,"bold"))
canvas.grid(row=1, column=1)

window.mainloop()