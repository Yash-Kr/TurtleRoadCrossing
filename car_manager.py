from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        random_choice = random.randint(1,7)
        if random_choice == 6:
            new_car = Turtle("square")  #each car will be a turtle object ( which we have imported to use here )
            new_car.shapesize(stretch_wid=1.0, stretch_len=2.0)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.seth(180)
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.cars_list.append(new_car)


    def move_cars(self):
        for car in self.cars_list:
            if car.xcor() < -300:
                self.cars_list.remove(car)
                car.ht()

            car.forward(self.speed)


    def increase_level(self):
        self.speed += MOVE_INCREMENT

