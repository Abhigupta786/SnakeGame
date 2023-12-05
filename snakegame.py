from turtle import Turtle , Screen
import time
from snake import *
from food import Food
from score import Score
sc=Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)
sc.listen()
snake=Snake()
food=Food()
score=Score()
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")
sc.onkey(snake.left,"Left")
sc.onkey(snake.right,"Right")


game=True
while game:
    sc.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase()
        snake.extend()
    if snake.head.xcor()>290 or snake.head.xcor()<-310 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.gameover()
        game=False
    for segment in snake.segments[1:]:
         
        if snake.head.distance(segment)<10:
            score.gameover()
            game=False
sc.exitonclick()