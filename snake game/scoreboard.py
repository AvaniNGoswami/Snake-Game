from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,280)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.write(f"Score : {self.score}",24)

    def incre_score(self):
        self.clear()
        self.goto(0, 280)
        self.score += 1
        self.write(f"Score : {self.score}",24)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", 24)
