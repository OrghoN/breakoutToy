# Internal Dependencies
from dataStructures import *
from configuration import *

def borderCollisionBall(ball):
    if ((ball.center.x - ball.radius) < 0 or ((ball.center.x + ball.radius) > INITIAL_WIDTH)):
        velocity = Point(-ball.velocity.x, ball.velocity.y)
    elif ((ball.center.y - ball.radius) < 0):
        velocity = Point(ball.velocity.x, -ball.velocity.y)
    else:
        velocity = Point(ball.velocity.x, ball.velocity.y)
    return Ball(ball.center, ball.radius, ball.color, velocity, ball.graphical)

def rectangleCollisionBall(rectangle, ball):
    return (ball.center.x > rectangle.topLeft.x and ball.center.x < rectangle.bottomRight.x and ball.center.y > rectangle.topLeft.y and ball.center.y < rectangle.bottomRight.y)

def paddleCollisionBall(paddle,ball):
    if rectangleCollisionBall(paddle, ball):
        velocity = Point(ball.velocity.x, -ball.velocity.y)
    else:
        velocity = Point(ball.velocity.x, ball.velocity.y)
    return Ball(ball.center, ball.radius, ball.color, velocity, ball.graphical)

def brickCollisionBall(bricks, ball):
    for brickNo, brick in enumerate(bricks):
        if rectangleCollisionBall(brick, ball):
            health = brick.health -1
            bricks[brickNo] = Brick(brick.topLeft, brick.bottomRight, brick.color, health, brick.graphical)
            velocity = Point(ball.velocity.x, -ball.velocity.y)
            return (brickNo, Ball(ball.center, ball.radius, ball.color, velocity, ball.graphical))
    return (False,ball)
