from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",22,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=ALIGNMENT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="Center",font=("Arial",22,"normal"))

        
    def increase_score(self):
        self.score+=1
        self.clear(    )
        self.update_scoreboard()

