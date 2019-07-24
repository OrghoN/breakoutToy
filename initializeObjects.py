# External Dependencies
import tkinter

# Internal Dependencies
from dataStructures import *
from configuration import *

def setupWindow():
    master = tkinter.Tk()
    master.title(TITLE)
    canvas = tkinter.Canvas(master, width = INITIAL_WIDTH, height = INITIAL_HEIGHT)
    # canvas.pack(side="bottom", fill="both", expand=True)
    canvas.pack()
    return canvas

# Make initial objects
def makeBricks():
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
            map.append(Brick(topLeft,bottomRight,colors[i%2],1))

    return map

# def makeBall():
