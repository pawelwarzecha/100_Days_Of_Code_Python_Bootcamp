import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")
counter = 0
difficulty = 5

scoreboard.level()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter == difficulty:
        car_manager.create_car()
        counter = 0  # Reset counter
    else:
        counter += 1

    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 300:
        player.goto(STARTING_POSITION)
        car_manager.increase_speed()
        scoreboard.level_number += 1
        scoreboard.level()

screen.exitonclick()