from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Create cards to drive across screen with random placement
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        x_cor = random.randint(-280, 300)
        y_cor = random.randint(-220, 280)
        self.color(COLORS[random.randint(0, 5)])
        self.goto(x=x_cor, y=y_cor)

    def auto_drive(self):
        self.goto(x=self.xcor() + MOVE_INCREMENT, y=self.ycor())

    # Method to replace car at random spot when it hit end of window
    def car_restart(self):
        if self.xcor() > 300:
            x_cor = -270
            y_cor = random.randint(-255, 270)
            self.goto(x=x_cor, y=y_cor)
