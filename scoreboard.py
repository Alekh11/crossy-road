from turtle import Turtle  

FONT = ("Courier", 18, "bold")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-250,250)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font= FONT)

    def increase_level(self):
        self.level += 1 
        self.update_scoreboard() 
        
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font = FONT)