# External Dependencies
import tkinter

# Internal Dependencies
from dataStructures import *
from configuration import *
import initializeObjects as initialize

def drawBricks(canvas, bricks):
    for brick in bricks:
        canvas.create_rectangle(brick.topLeft.x, brick.topLeft.y, brick.bottomRight.x, brick.bottomRight.y, fill=brick.color)


canvas = initialize.setupWindow()
bricks = initialize.makeBricks()


drawBricks(canvas, bricks)

tkinter.mainloop()
