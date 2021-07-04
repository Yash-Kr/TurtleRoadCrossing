from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

        self.penup()
        self.ht()
        self.goto(-200, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}",align="center", font=FONT )

