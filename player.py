from turtle import Turtle

import scoreboard
from scoreboard import Scoreboard

STARTING_POSITION = (20, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Car class to create car objects
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.right(270)
        self.goto(STARTING_POSITION)

    # Make Turtle move on the screen
    def move(self):
        new_y = self.ycor() + 10
        self.goto(x=self.xcor(), y=new_y)

        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
