# External Dependencies
import tkinter
import time
import functools

# Internal Dependencies
from dataStructures import *
from configuration import *
import initializeObjects as initialize
import collision
import move

canvas = initialize.setupWindow()

bricks = initialize.makeBricks(canvas)
ball = initialize.makeBall(canvas, BALL_ORIGIN, BALL_RADIUS, BALL_COLOR, BALL_VELOCITY)
paddle = initialize.makePaddle(canvas, PADDLE_ORIGIN, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_COLOR)

cursorPosition = Point(0,0)
while True:
    ball = collision.borderCollisionBall(ball)
    ball = collision.paddleCollisionBall(paddle, ball)
    brickNo, ball = collision.brickCollisionBall(bricks, ball)

    move.cleanBricks(canvas, brickNo, bricks)
    ball = move.moveBall(canvas, ball)

    paddle = move.movePaddle(canvas, paddle)

    canvas.update()
    time.sleep(0.01)

tkinter.mainloop()
