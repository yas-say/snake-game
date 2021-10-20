from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



flag = True

while flag:
    screen.update()
    sleep(0.1)
    snake.move()

    #Detect collision
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()

screen.update()
screen.exitonclick()

