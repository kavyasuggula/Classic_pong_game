from paddle import *
from ball import *
from score import *

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong")

left_paddle = Paddle()
right_paddle = Paddle()

# key events
screen.listen()
screen.onkey(left_paddle.upwards, "w")
screen.onkey(left_paddle.downwards, "s")
screen.onkey(right_paddle.upwards, "Up")
screen.onkey(right_paddle.downwards, "Down")



screen.tracer(0)

for segment in range(5):
    left_paddle.create_paddle(segment, -1)
    right_paddle.create_paddle(segment, 1)
total_paddles = [left_paddle, right_paddle]
score = Score()
ball = Ball()

screen.update()

game_on = True
while game_on:
    screen.update()

    sleep(0.075)
    l_game_on = left_paddle.motion(left_paddle.up)
    r_game_on = right_paddle.motion(right_paddle.up)
    b_game_on = ball.movement(total_paddles)
    score.update_score(ball.left_paddle_hits,ball.right_paddle_hits)
    if not(l_game_on and r_game_on and b_game_on):
        game_on = False

game = Turtle()
game.color("red")
game.hideturtle()
game.write("Game Over!!", align="center", font=("arial", 24, "bold"))

screen.exitonclick()