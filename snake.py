from turtle import Turtle, Screen

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

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
        self.snake_segments[0].left(90)
        self.snake_segments[0].forward(20)
