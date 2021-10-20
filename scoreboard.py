from turtle import Turtle

ALIGNMENT = "center"
FONTA = ('Arial', 10, 'bold')
FONTB = ('Arial', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.score_display()

    def score_display(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Total Score: {self.score}", move=False, align=ALIGNMENT, font=FONTA)

    def score_increase(self):
        self.score += 1
        self.score_display()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONTB)