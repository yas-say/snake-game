from turtle import Turtle, Screen

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for _ in START_POSITION:
            t1 = Turtle("square")
            t1.color("white")
            t1.penup()
            t1.goto(_)
            self.snake_segments.append(t1)

    def move(self):
        for _ in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[_].goto(self.snake_segments[_ - 1].xcor(), self.snake_segments[_ - 1].ycor())
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
