from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [-250, -230, -210, -190, -170, -150, -130, -110, -90, -70, -50, -30, -10,
             10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
            car = Turtle("square")
            car.penup()
            car.shapesize(1,2)
            car.color(random.choice(COLORS))
            car.goto(300,random.choice(POSITIONS))
            car.setheading(180)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT



