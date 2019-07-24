import tkinter
from collections import namedtuple

#Define Data Structures
Point = namedtuple('Point', ['x', 'y'])
Ball = namedtuple('Ball', ['center', 'radius', 'color', 'velocity'])
Brick = namedtuple('Brick', ['bottomLeft', 'topRight', 'color', 'health'])
Paddle = namedtuple('Paddle', ['bottomLeft', 'topRight', 'color'])

#Define initial Parameters
INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 900

def setupWindow():
    master = tkinter.Tk()
    canvas = tkinter.Canvas(master, width = INITIAL_WIDTH, height = INITIAL_HEIGHT)
    # canvas.pack(side="bottom", fill="both", expand=True)
    canvas.pack()


setupWindow()
tkinter.mainloop()
