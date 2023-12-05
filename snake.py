from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
LEFT=180
RIGHT=0
DOWN=270
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for posit in STARTING_POSITIONS:
            self.add_segments(posit)
    def add_segments(self,posit):
        segment=Turtle("square")
        segment.color("white")
        segment.penup()
        segment.speed("slow")
        segment.goto(posit)
        self.segments.append(segment)
    def extend(self):
        self.add_segments(self.segments[-1].pos())
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            post=self.segments[seg_num-1].pos()
            self.segments[seg_num].goto(post)
        self.head.forward(MOVE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)