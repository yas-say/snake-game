from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
s_board = Scoreboard()

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
        s_board.score_increase()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        s_board.game_over()
        flag = False


screen.update()
screen.exitonclick()

