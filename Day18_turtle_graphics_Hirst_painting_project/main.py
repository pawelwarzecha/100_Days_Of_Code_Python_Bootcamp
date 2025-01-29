import turtle
import colorgram
import random

colors = colorgram.extract('image.jpg', 30)

rgb = []

for color in colors:
    rgb.append((color.rgb.r, color.rgb.g, color.rgb.b))

color_list = [(2, 9, 30), (244, 238, 243), (122, 95, 42), (72, 32, 22), (237, 212, 72), (220, 81, 59), (225, 117, 100), (92, 1, 21), (178, 140, 170), (150, 92, 115), (34, 90, 27), (8, 154, 73), (204, 63, 91), (168, 129, 78), (2, 64, 146), (3, 78, 28), (5, 220, 218), (220, 179, 218), (79, 135, 179), (81, 113, 141), (126, 154, 176), (116, 187, 167), (10, 215, 221), (119, 15, 34), (136, 222, 207), (242, 205, 9), (229, 174, 165)]

timmy = turtle.Turtle()
timmy.hideturtle()
turtle.colormode(255)
timmy.speed("fastest")

timmy.penup()
timmy.goto(-340, -270)
timmy.pendown()
row = 0
column = 0
height = -270

while column < 10:
    while row < 10:
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(75)
        timmy.pendown()
        row += 1
    row = 0
    height += 60
    timmy.penup()
    timmy.goto(-340, height)
    timmy.pendown()
    column += 1

screen = turtle.Screen()
screen.exitonclick()


