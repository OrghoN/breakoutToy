# External Dependencies
import tkinter

# Internal Dependencies
from dataStructures import *
from configuration import *
import initializeObjects as initialize

def drawBricks(canvas, bricks):
    for brick in bricks:
        canvas.create_rectangle(brick.topLeft.x, brick.topLeft.y, brick.bottomRight.x, brick.bottomRight.y, fill=brick.color)

def drawBall(canvas, ball):
    canvas.create_oval(ball.center.x - ball.radius, ball.center.y - ball.radius, ball.center.x + ball.radius, ball.center.y + ball.radius, fill = ball.color, width=0)

def drawPaddle(canvas, paddle):
    canvas.create_rectangle(paddle.topLeft.x, paddle.topLeft.y, paddle.bottomRight.x, paddle.bottomRight.y, fill=paddle.color)

canvas = initialize.setupWindow()

bricks = initialize.makeBricks(canvas)
ball = initialize.makeBall(canvas, BALL_ORIGIN, BALL_RADIUS, BALL_COLOR, BALL_VELOCITY)
paddle = initialize.makePaddle(canvas, PADDLE_ORIGIN, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_COLOR)

tkinter.mainloop()
