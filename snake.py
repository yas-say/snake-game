from turtle import Turtle, Screen
from time import sleep

class Snake:
    def __init__(self):
        start_position = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
        snake = []

        for _ in start_position:
            t1 = Turtle("square")
            t1.color("white")
            t1.penup()
            t1.goto(_)
            snake.append(t1)