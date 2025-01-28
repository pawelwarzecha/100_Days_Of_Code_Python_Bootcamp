from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level_number = 0

    def level(self):
        self.clear()
        self.penup()
        self.goto(-200, 250)
        self.pendown()
        self.write(f"Level: {self.level_number}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write("GAME OVER!", align="center", font=FONT)
