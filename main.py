import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")


print("Hello")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision of player
    for car in car_manager.cars_list:
        if player.distance(car) < 20:
            screen.update()
            game_is_on = False
            break

    #detect if player successfully crosses the road
    if player.wins():
        score.update_level()
        car_manager.increase_level()


screen.exitonclick()

