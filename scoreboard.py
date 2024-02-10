from turtle import Turtle

FONT = ("Courier", 20, "bold")
LOCATION = (0, 575)


# Class to keep score of game
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.clear()
        self.color("black")
        self.score = 0
        self.setposition(-220, 269)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    # Method to increase score
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.setposition(-80,200)
        self.write("Game Over", font=FONT)
