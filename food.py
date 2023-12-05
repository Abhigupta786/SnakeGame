from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x_cor=randint(-280,280)
        y_cor=randint(-280,280)
        self.goto(x_cor,y_cor)
        