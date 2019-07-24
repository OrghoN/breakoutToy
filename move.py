# Internal Dependencies
from dataStructures import *
from configuration import *

def moveBall(canvas, ball):
    position = Point(ball.center.x + ball.velocity.x, ball.center.y + ball.velocity.y)
    canvas.move(ball.graphical, ball.velocity.x, ball.velocity.y)

    return Ball(position, ball.radius, ball.color, ball.velocity, ball.graphical)

def movePaddle(canvas, paddle):
    cursorPosition = canvas.winfo_pointerx()
    paddleWidth = paddle.bottomRight.x - paddle.topLeft.x
    topLeft = Point(int(cursorPosition - paddleWidth/2), paddle.topLeft.y)
    bottomRight = Point(int(cursorPosition + paddleWidth/2), paddle.bottomRight.y)

    # Edge detection for paddle
    if(topLeft.x < 0):
        topLeft = Point(0, paddle.topLeft.y)
        bottomRight = Point(paddleWidth, paddle.bottomRight.y)
    elif(bottomRight.x > INITIAL_WIDTH):
        topLeft = Point(INITIAL_WIDTH - paddleWidth, paddle.topLeft.y)
        bottomRight = Point(INITIAL_WIDTH, paddle.bottomRight.y)

    velocity = Point(topLeft.x - paddle.topLeft.x,0)
    canvas.move(paddle.graphical, velocity.x, velocity.y)

    return Paddle(topLeft,bottomRight, paddle.color, paddle.graphical)

def cleanBricks(canvas, brickNo, bricks):
    if(brickNo or brickNo == 0):
        brick = bricks[brickNo]
        if (brick.health <=0):
            canvas.delete(brick.graphical)
            del bricks[brickNo]
