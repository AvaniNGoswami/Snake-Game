from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segs[0].distance(food)<15:
        food.redirect_food()
        scoreboard.incre_score()
        snake.extend()

    if snake.segs[0].xcor()>280 or snake.segs[0].xcor()<-280 or snake.segs[0].ycor()>280 or snake.segs[0].ycor()<-280:
        game_is_on = False
        scoreboard.game_over()

    for i in snake.segs:
        if i == snake.segs[0]:
            pass
        elif snake.segs[0].distance(i)<15:
            game_is_on = False
            scoreboard.game_over()









screen.exitonclick()
