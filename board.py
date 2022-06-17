import tkinter as t
import tkinter.font


def resetBoard():
    """
    Starts the game: for the given column and row size, this function makes a grid of buttons with a text value of 0
    Buttons are from tkinter and on press, execute a command (function). All attributes of button are defined
    """
    turn.set(0)

    for x in range(rowSize):
        for y in range(colSize):
            value = 0
            val[x][y] = t.StringVar()
            btn[x][y] = t.Button(frame, textvariable=val[x][y], command=lambda x=x, y=y: add(x, y))
            btn[x][y]["width"] = 5
            btn[x][y]["height"] = 3
            btn[x][y]["bg"] = "black"
            btn[x][y]["fg"] = "white"
            btn[x][y]["activebackground"] = "white"
            btn[x][y]["activeforeground"] = "white"
            btn[x][y]["font"] = fontForGame
            val[x][y].set(value)
            btn[x][y].grid(row=x, column=y)


def add(x, y):
    """
    Funtion run when button is clicked
    """
    if btn[x][y]["bg"] == color[turn.get() % playersCount] or btn[x][y]["bg"] == "black":
        addAtom(x, y)
        nextPLayer()


def addAtom(x, y):
    """
    Adds a point to the selected cell by user and explodes it if it exceeds max value
    :param x: row no
    :param y: column no
    """
    value = 1 + int(val[x][y].get())

    if value > maxSize(x, y):
        return

    btn[x][y]["bg"] = color[turn.get() % playersCount] #color[1]

    if value == maxSize(x, y):
        btn[x][y]["bg"] = "black"
        val[x][y].set(0)
        explode(x, y)
        btn[x][y].flash()
    else:
        val[x][y].set(value)


def explode(x, y):
    """
    When a cell equals max size, it splits into all possible adjacent spaces
    :param x: row no
    :param y: column no
    """
    if x - 1 >= 0:
        # up
        addAtom(x - 1, y)
    if x + 1 <= rowSize - 1:
        # down
        addAtom(x + 1, y)
    if y - 1 >= 0:
        # left
        addAtom(x, y - 1)
    if y + 1 <= colSize - 1:
        # right
        addAtom(x, y + 1)
    return


def maxSize(x, y):
    """
    :param x: row no
    :param y: column no
    :return: maximum value a cell can hold depending on position (corner, edge, middle)
    """
    size = 4
    if x == rowSize - 1 or x == 0:
        size -= 1
    if y == colSize - 1 or y == 0:
        size -= 1
    return size


def nextPLayer():
    """
    change turns
    """
    turn.set(turn.get() + 1)



window = t.Tk()

# font style
fontForGame = tkinter.font.Font(family='Times', size=15, weight='bold')

# it's just an integer with more options/functions
turn = t.IntVar()

frame = t.Frame(window)
frame.pack()

# custom game details
rowSize = 5
colSize = 5

playersCount = 2
color = ["red", "lime"]

# creating a 2d array with 0 as all values
btn = [[0 for y in range(colSize)] for x in range(rowSize)]
val = [[0 for y in range(colSize)] for x in range(rowSize)]

# the function that starts the game
resetBoard()

# waits for user input like button press
window.mainloop()
