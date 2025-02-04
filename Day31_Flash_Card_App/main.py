from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
words_dict = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(words_dict)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)

def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")

def remove_word():
    words_dict.remove(current_card)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR ,padx=50, pady=50)

timer = window.after(3000, func=flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR ,width=800, height=526, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "bold"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

wrong = PhotoImage(file="images/wrong.png")
reject_button = Button(image=wrong, highlightthickness=0, command=next_card)
reject_button.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
confirm_button = Button(image=right, highlightthickness=0, command=remove_word)
confirm_button.grid(row=1,column=1)

next_card()

window.mainloop()