from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Here we declare all these constants because if we want to
# change something related to them, we must look at the top of our code
# instead looking through our entire code


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        # Creating three segments and using tuples to position them in the right way
        for position in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)

    def move(self):
        # change the way our snake moves, now it moves from the last square to the first one
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() == 0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)

    def down(self):
        if self.segments[0].heading() == 0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)

    def left(self):
        if self.segments[0].heading() == 90:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].right(90)

    def right(self):
        if self.segments[0].heading() == 90:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].left(90)

