# External Dependencies
import tkinter

# Internal Dependencies
from dataStructures import *
from configuration import *

def setupWindow():
    master = tkinter.Tk()
    master.title(TITLE)
    canvas = tkinter.Canvas(master, width = INITIAL_WIDTH, height = INITIAL_HEIGHT)
    # canvas.pack(fill="both", expand=True)
    canvas.pack()

    #draw Borders
    canvas.create_line(0, 0, 0, INITIAL_HEIGHT, fill=BORDER_COLOR, width=3)
    canvas.create_line(0, 0, INITIAL_WIDTH, 0, fill=BORDER_COLOR, width=3)
    # canvas.create_line(0, INITIAL_HEIGHT, INITIAL_WIDTH, INITIAL_HEIGHT, fill=BORDER_COLOR, width=1)
    canvas.create_line(INITIAL_WIDTH, 0, INITIAL_WIDTH, INITIAL_HEIGHT, fill=BORDER_COLOR, width=1)
    return canvas

# Make initial objects
def makeBricks(canvas):
    #Boundaries of the map
    left = int(0.05 * INITIAL_WIDTH)
    right = int(INITIAL_WIDTH - left)
    top = int(0.05 * INITIAL_HEIGHT)
    bottom = int(0.45 * INITIAL_HEIGHT)

    #Gap between bricks
    horizontalGap = int(0.02 * INITIAL_WIDTH)
    verticalGap = int(0.03 * INITIAL_HEIGHT)

    #Number of Rows and Columns
    rows = 5
    columns = 11

    #Brick Size
    brickWidth = int(right - left - horizontalGap*columns)/(columns)
    brickHeight = (bottom - top - verticalGap*rows)/(rows)

    # Brick color
    colors = ["#147fb3", "#b33514"]

    map = []

    for i in range (0,columns):
        for j in range (0,rows):
            topLeft = Point(int(left + brickWidth * i + horizontalGap * (i+0.5)), int(top + brickHeight * j + verticalGap * j))
            bottomRight = Point(int(left + brickWidth * i + horizontalGap * (i+0.5) + brickWidth ), int(top + brickHeight * j + verticalGap * j + brickHeight))
            color = colors[i%2]
            graphical = canvas.create_rectangle(topLeft.x, topLeft.y, bottomRight.x, bottomRight.y, fill=color)
            map.append(Brick(topLeft, bottomRight, color, 1, graphical))

    return map

def makeBall(canvas, origin, radius, color, velocity):
    graphical = canvas.create_oval(origin.x - radius, origin.y - radius, origin.x + radius, origin.y + radius, fill = color, width=0)
    return Ball(origin, radius, color, velocity, graphical)

def makePaddle(canvas, origin, height, width, color):
    topLeft = Point(int(origin.x - width/2), int(origin.y - height/2))
    bottomRight = Point(int(origin.x + width/2), int(origin.y + height/2))
    graphical = canvas.create_rectangle(topLeft.x, topLeft.y, bottomRight.x, bottomRight.y, fill=color)
    return Paddle(topLeft, bottomRight, color, graphical)
