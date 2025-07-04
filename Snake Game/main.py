from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def draw_border():
    border = Turtle()
    border.hideturtle()
    border.color("gray")
    border.penup()
    border.goto(-290, -290)
    border.pendown()
    border.pensize(3)
    for _ in range(4):
        border.forward(580)
        border.left(90)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game - Upgraded UI")
screen.tracer(0)
draw_border()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Instructions before game starts
intro = Turtle()
intro.hideturtle()
intro.color("white")
intro.penup()
intro.goto(0, 0)
intro.write("Press Arrow Keys to Start!", align="center", font=("Arial", 18, "normal"))

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Wait for user input
screen.update()
time.sleep(1)
intro.clear()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
