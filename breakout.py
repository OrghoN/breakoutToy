import tkinter

INITIAL_WIDTH = 1600
INITIAL_HEIGHT = 900

def setupWindow():
    master = tkinter.Tk()
    canvas = tkinter.Canvas(master, width = INITIAL_WIDTH, height = INITIAL_HEIGHT)
    # canvas.pack(side="bottom", fill="both", expand=True)
    canvas.pack()


setupWindow()
tkinter.mainloop()
