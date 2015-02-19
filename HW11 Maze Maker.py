# John M Flaherty HW11

from Tkinter import *
import time
import random

maxDepth = 0
maxDepthRow = 0
maxDepthCol = 0

COLS = 30
ROWS = 30
CELL_SIZE = 20

OPEN = 1
CLOSED = 2
UNKNOWN = 3
START = 4
FINISH = 5

root = Tk()
root.title("Maze Maker")

canvas = Canvas(root, height = CELL_SIZE * COLS, width = CELL_SIZE * ROWS)
canvas.grid(row = 0, column = 0)

board = []
values = []

for row in range(ROWS):
    board.append([])
    values.append([])
    for col in range(COLS):
        x = row*CELL_SIZE
        y = col*CELL_SIZE
        x2 = (row+1)*(CELL_SIZE)-1
        y2 = (col+1)*(CELL_SIZE)-1
        rect = canvas.create_rectangle(x,y,x2,y2)
        board[row].append(rect)
        canvas.itemconfig(rect, fill = "black")
        canvas.update()
        values[row].append(UNKNOWN)

def changeRectangle(row, col):
    currentCell = board[row][col]
    state = values[row][col]
    
    if state == OPEN:
        canvas.itemconfig(board[row][col], fill = "green")
    if state == START or state == FINISH:
        canvas.itemconfig(board[row][col], fill = "red")
    if state == CLOSED:
        canvas.itemconfig(board[row][col], fill = "black")
    canvas.update()
    time.sleep(0.01)

for i in range(ROWS):
    values[0][i] = CLOSED
    changeRectangle(0,i)
    values[29][i] = CLOSED
    changeRectangle(29,i)
    values[i][0] = CLOSED
    changeRectangle(i,0)
    values[i][29] = CLOSED
    changeRectangle(i, 29)

def solveCell(row, col, depth):
    state = values[row][col]
    if state != UNKNOWN:
        return
    count = 0
    if values[row+1][col] == OPEN:
        count += 1
    if values[row-1][col] == OPEN:
        count += 1
    if values[row][col+1] == OPEN:
        count += 1
    if values[row][col-1] == OPEN:
        count += 1
    if count > 1:
        values[row][col] = CLOSED
        changeRectangle(row, col)
        canvas.update()
        time.sleep(0.01)
        return
    
    values[row][col] = OPEN
    changeRectangle(row, col)
    canvas.update()
    time.sleep(0.01)

    global maxDepth
    global maxDepthRow
    global maxDepthCol

    neighborList = [[row+1,col],[row,col+1],[row-1,col],[row,col-1]]
    random.shuffle(neighborList)

    for i in range(len(neighborList)):
        r = neighborList[i][0]
        c = neighborList[i][1]
        solveCell(r, c, depth+1)

    if depth > maxDepth:
        maxDepth = depth
        maxDepthRow = row
        maxDepthCol = col

solveCell(1,1,1)
values[1][1] = START
changeRectangle(1,1)
values[maxDepthRow][maxDepthCol] = FINISH
changeRectangle(maxDepthRow, maxDepthCol)
    
root.mainloop()
