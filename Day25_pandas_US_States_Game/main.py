import turtle
import pandas
import tkinter as tk
from tkinter import messagebox

def show_message(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title=title, message=message)
    root.destroy()

def write_state_name(state):
    row = data[data["state"] == state]
    x_cor = row["x"].values[0]
    y_cor = row["y"].values[0]
    writer_turtle = turtle.Turtle()
    writer_turtle.hideturtle()
    writer_turtle.penup()
    writer_turtle.goto(x_cor, y_cor)
    writer_turtle.write(state, align="center")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = [item for item in states_list if item not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in guessed_states:
        show_message("Already guessed",f"Already guessed {answer_state}")
    elif answer_state in states_list:
        guessed_states.append(answer_state)
        write_state_name(answer_state)
        screen.title(f"{len(guessed_states)}/50 States Correct")

    if len(guessed_states) == 50:
        show_message("You Won!", "You guessed all 50 states correctly!")