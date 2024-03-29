# Internal Dependencies
from dataStructures import *

#Define initial Parameters
INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 900
TITLE = "Breakout"

BORDER_COLOR = "#202020"

PADDLE_HEIGHT = int(INITIAL_HEIGHT * 0.02)
PADDLE_WIDTH = int(INITIAL_WIDTH*0.2)
PADDLE_ORIGIN = Point(int(INITIAL_WIDTH/2),int(INITIAL_HEIGHT - PADDLE_HEIGHT/2))
PADDLE_COLOR = "#14b34e"

BALL_RADIUS = int(INITIAL_HEIGHT * 0.015)
BALL_ORIGIN = Point(PADDLE_ORIGIN.x, PADDLE_ORIGIN.y - PADDLE_HEIGHT/2 - BALL_RADIUS)
BALL_COLOR = "#14b34e"
BALL_VELOCITY = Point(5,-5)
