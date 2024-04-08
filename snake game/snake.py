from turtle import Turtle

POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    def __init__(self):
        self.segs = []
        self.create_snake()

    def create_snake(self):
        for i in POSITION:
            self.add_seg(i)


    def add_seg(self,i):
        new_seg = Turtle()
        new_seg.penup()
        new_seg.goto(i)
        new_seg.shape("square")
        new_seg.color("white")
        self.segs.append(new_seg)

    def extend(self):
        self.add_seg(self.segs[-1].position())

    def move(self):
        for i in range(len(self.segs)-1, 0, -1):
            new_x = self.segs[i-1].xcor()
            new_y = self.segs[i-1].ycor()
            self.segs[i].goto(new_x, new_y)
        self.segs[0].forward(20)

    def up(self):
        if self.segs[0].heading() != DOWN:
            self.segs[0].setheading(90)

    def down(self):
        if self.segs[0].heading() != UP:
            self.segs[0].setheading(270)

    def right(self):
        if self.segs[0].heading() != LEFT:
            self.segs[0].setheading(0)

    def left(self):
        if self.segs[0].heading() != RIGHT:
            self.segs[0].setheading(180)







