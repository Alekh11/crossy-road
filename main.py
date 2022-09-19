import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up ,"Up") 


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    carmanager.create_cars()
    carmanager.move_cars()
    
    #detect collison:
    for car in carmanager.all_cars:
        if car.distance(player)<30:
            game_is_on = False 
            scoreboard.gameover()
            
    #if crossing is completed:
    if player.at_finishline():
        player.go_to_start()
        carmanager.levelup()
        scoreboard.increase_level()

screen.exitonclick()