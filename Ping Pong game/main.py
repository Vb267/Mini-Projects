from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Create game objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Movement flags
r_up = False
r_down = False
l_up = False
l_down = False


# Key press/release handlers
def r_up_press():
    global r_up
    r_up = True


def r_up_release():
    global r_up
    r_up = False


def r_down_press():
    global r_down
    r_down = True


def r_down_release():
    global r_down
    r_down = False


def l_up_press():
    global l_up
    l_up = True


def l_up_release():
    global l_up
    l_up = False


def l_down_press():
    global l_down
    l_down = True


def l_down_release():
    global l_down
    l_down = False


# Bind keys
screen.listen()
screen.onkeypress(r_up_press, "Up")
screen.onkeyrelease(r_up_release, "Up")
screen.onkeypress(r_down_press, "Down")
screen.onkeyrelease(r_down_release, "Down")

screen.onkeypress(l_up_press, "w")
screen.onkeyrelease(l_up_release, "w")
screen.onkeypress(l_down_press, "s")
screen.onkeyrelease(l_down_release, "s")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    # Move paddles smoothly
    if r_up:
        r_paddle.go_up()
    if r_down:
        r_paddle.go_down()
    if l_up:
        l_paddle.go_up()
    if l_down:
        l_paddle.go_down()

    # Ball movement
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Missed ball
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
