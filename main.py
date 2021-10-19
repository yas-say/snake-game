from turtle import Turtle, Screen
from time import sleep
from snake import Snake

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

snake = Snake()

flag = True

while flag:
    screen.update()
    sleep(0.5)
    snake.move()



screen.exitonclick()

