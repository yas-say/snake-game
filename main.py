from turtle import Turtle, Screen
from time import sleep
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# t1 = Turtle("square")
# t2 = Turtle("square")
# t3 = Turtle("square")
#
# t1.color("white")
# t2.color("green")
# t3.color("yellow")
#
# #print(t1.turtlesize())
# #t1.shapesize(1, 3, 1)
#
# tup = t1.position()
# t2.goto(t1.xcor()-20,t1.ycor())
# t3.goto(t2.xcor()-20,t2.ycor())

start_position = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
snake = []

for _ in start_position:
    t1 = Turtle("square")
    t1.color("white")
    t1.penup()
    t1.goto(_)
    snake.append(t1)


flag = True

while flag:
    screen.update()
    sleep(0.5)
    for _ in range(len(snake)-1, 0, -1):
        snake[_].goto(snake[_-1].xcor(),snake[_-1].ycor())
    snake[0].left(90)
    snake[0].forward(20)


screen.exitonclick()

