import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import  Scoreboard
from scoreboard import Scoreboard

# Use list to create car objects with name using number

car_list = ["car1", "car2", "car3", "car4", "car5", "car6", "car7", "car8", "car9", "car10"]
car_ojb = []
for car in car_list:
    car = CarManager()
    car_ojb.append(car)

print(car_ojb)