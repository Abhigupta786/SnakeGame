from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.score=0
        self.hideturtle()
        self.update()
    def update(self):
        self.write(f"Score: {self.score}",move=False,align=ALIGNMENT,font=FONT)
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over",move=False,align=ALIGNMENT,font=FONT)

    def increase(self):
        self.score+=1
        self.clear()
        self.update()