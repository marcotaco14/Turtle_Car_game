import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

# Speed of loop increases with each point scored
speed = 0.1
# Create score object
score = Scoreboard()
FONT = ("Arial", 24, "normal")
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Welcome to Car Game!!!")
player = Player()

# Use list names to create car objects
car_list = ["car1", "car2", "car3", "car4", "car5", "car6", "car7", "car8", "car9", "car10"]
car_ojb = []
for car in car_list:
    car = CarManager()
    car_ojb.append(car)

game_is_on = True

# Move car
screen.listen()
screen.onkey(fun=player.move, key="Up")

# While loop to run game
while game_is_on:
    time.sleep(speed)
    screen.update()
    # Create cars to drive across the screen
    for x in car_ojb:
        x.auto_drive()
    # Keep cars running when they hit end of screen
    for x in car_ojb:
        if x.xcor() > 300:
            x.car_restart()

    # Detect contact with cars and player
    for x in car_ojb:
        if player.distance(x) < 20:
            #player.write(f"Game Over", align="center", font=FONT)
            score.game_over()
            game_is_on = False
    # Increase score when turtle reaches end, put back in beginning, keep cars moving
    if player.ycor() > 268:
        score.increase_score()
        player.move()
        car.auto_drive()
        speed -= 0.01


screen.exitonclick()
