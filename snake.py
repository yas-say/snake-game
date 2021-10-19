from turtle import Turtle, Screen


start_position = [(0, 0), (-20, 0), (-40, 0)]
snake = []

class Snake:
    def __init__(self):
       for _ in start_position:
           t1 = Turtle("square")
           t1.color("white")
           t1.penup()
           t1.goto(_)
           snake.append(t1)

    def move(self):
        for _ in range(len(snake) - 1, 0, -1):
            snake[_].goto(snake[_ - 1].xcor(), snake[_ - 1].ycor())
        snake[0].left(90)
        snake[0].forward(20)
