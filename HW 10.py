# John M Flaherty HW 9

from Tkinter import *
import tkFileDialog

root = Tk()
root.title("Sudoku")

EMPTY = ""

board = []
for row in range(9):
    board.append([])
    for col in range(9):
        if col%3==2 and col<8:
            paddingX=[1,5]
        else:
            paddingX=[1,1]
        if row%3==2 and row<8:
            paddingY=[1,5]
        else:
            paddingY=[1,1]
        e = Entry(root, width=3, justify=CENTER)
        e.grid(row=row+1, column=col, padx=paddingX, pady=paddingY)
        board[row].append(e)
        
resultEntry = Entry(root, justify=CENTER)
resultEntry.grid(row=11, column=0, columnspan=9, sticky="NESW")

def checkBoard():
    for row in range(9):
        for col in range(9):
            if board[row][col].get()!=EMPTY:
                if checkCell(row,col) == False:
                    resultEntry.delete(0,END)
                    resultEntry.insert(0,"There is an inconsistency")
                    return
    resultEntry.delete(0,END)
    resultEntry.insert(0,"Board is consistent")

def clear():
    for row in range(9):
        for col in range(9):
            board[row][col].delete(0, END)

def checkCell(row,col):
    val = board[row][col].get()
    if checkRow(row,val) == True and checkCol(col,val) == True and checkCluster(row,col,val) == True:
        return True
    else:
        return False

def checkRow(row,val):
    count = 0
    for i in range(9):
        if board[row][i].get() == val:
            count += 1
    if count > 1:
        return False
    else:
        return True

def checkCol(col,val):
    count = 0
    for i in range(9):
        if board[i][col].get() == val:
            count += 1
    if count > 1:
        return False
    else:
        return True

def checkCluster(row,col,val):
    count = 0
    for r in range(row-row%3, (row-row%3)+3):
        for c in range(col-col%3, (col-col%3)+3):
            if board[r][c].get() == val:
                count += 1
    if count > 1:
        return False
    else:
        return True

def put(row, col, val):
    global board
    board[row][col].delete(0, END)
    board[row][col].insert(0, val)

def load():
    clear()
    filename = tkFileDialog.askopenfilename(initialdir = ".")
    fin = open(filename, "r")
    text = fin.read()
    fin.close()
    next = 0
    for row in range(9):
        for col in range(9):
            val = text[next]
            if val == "0":
                val = ""
            put(row, col, val)
            if val != "":
                board[row][col].config(fg = "RED")
            next += 1

def solve():
    for row in range(9):
        for col in range(9):
            if board[row][col].get() == EMPTY:
                for guess in range(1,10):
                    put(row, col, guess)
                    board[row][col].update()
                    if checkCell(row, col):
                        if solve():
                            return True
                board[row][col].delete(0,END)
                board[row][col].update()
                return False
    return True
            
checkButton = Button(root, text = "Check", command = checkBoard)
checkButton.grid(row=0, column = 0, columnspan = 3, sticky = "NSEW")
clearButton = Button(root, text = "Clear", command = clear)
clearButton.grid(row = 0, column = 3, columnspan = 3, sticky = "NSEW")
loadButton = Button(root, text = "Load", command = load)
loadButton.grid(row = 0, column = 6, columnspan = 3, sticky = "NSEW")
solveButton = Button(root, text = "Solve", command = solve)
solveButton.grid(row = 0, column = 9, columnspan = 3, sticky = "NSEW")
        
root.mainloop()
