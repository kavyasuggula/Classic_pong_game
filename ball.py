from turtle import Turtle
from paddle import *

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.left_paddle_hits = 0
        self.right_paddle_hits = 0

    def create_ball(self):
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=0.45,stretch_len=0.45)
        self.penup()


    def movement(self, Paddle):
        self.fd(10)
        self.ball_paddle_bounce(Paddle)
        self.ball_wall_bounce()
        return self.check_game()

    def check_game(self):
        self.x = self.xcor()
        if self.x >291 or self.x < -291:
            return False
        return True

    def ball_paddle_bounce(self, Paddle):
        self.right_paddle_bounce(Paddle[1])
        self.left_paddle_bounce(Paddle[0])


    def left_paddle_bounce(self,left_paddle):
        self.flag = 0
        for i in range(len(left_paddle.paddle)):
            if self.distance(left_paddle.paddle[i]) < 10:
                self.flag = 1
        if self.flag == 1:
            self.left_paddle_hits += 1
            if left_paddle.up == 0:
                    self.setheading(0)
            elif left_paddle.up == -1:
                    if self.heading() == 180:
                        self.setheading(60)
                    else:
                        if self.heading() > 180:
                            self.setheading(self.heading() - 180)
                        elif self.heading() < 180:
                            self.setheading(self.heading() - 90)

            elif left_paddle.up == 1:
                    if self.heading() == 180:
                        self.setheading(300)
                    else:
                        if self.heading() > 180:
                            self.setheading(self.heading() + 90)
                        elif self.heading() < 180:
                            self.setheading(self.heading() + 180)

    def right_paddle_bounce(self,right_paddle):
        self.flag = 0
        for i in range(len(right_paddle.paddle)):
            if self.distance(right_paddle.paddle[i]) < 20:
                self.flag = 1
        if self.flag == 1:
            self.right_paddle_hits += 1
            if right_paddle.up == 0:
                self.setheading(180)

            elif right_paddle.up == 1:
                if self.heading()==0:
                    self.setheading(120)
                else:
                    if self.heading() > 270:
                        self.setheading(self.heading() - 180)
                    elif self.heading() < 90:
                        self.setheading(self.heading() + 90)

            elif right_paddle.up == -1:
                if self.heading() == 0:
                    self.setheading(240)
                else:
                    if self.heading() > 270:
                        self.setheading(self.heading() - 90)
                    elif self.heading() < 180:
                        self.setheading(self.heading() + 180)

    def ball_wall_bounce(self):
        self.y = self.ycor()
        if self.y > 290 or self.y < -290:
            self.cur_heading = self.heading()
            if self.cur_heading < 90 :
                self.setheading(360- self.cur_heading)
            elif self.cur_heading < 180 :
                self.setheading(self.cur_heading + 90)
            elif self.cur_heading < 270 :
                self.setheading(self.cur_heading - 90)
            elif self.cur_heading < 360 :
                self.setheading(self.cur_heading + 90)

