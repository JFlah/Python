### Lists in lists
##
##a = [[1,2,82],[99,88],[9,0,93]]
##print a # gives all numbers
##print a[2] # gives [9, 0, 93]
##print a[2][0] # gives 9

# Tic Tac Toe

from Tkinter import *
root = Tk()
root.title("Tic Tac Toe")

X = "X"
O = "O"
empty = "."

##board = [   [empty, empty, empty],
##            [empty, empty, empty],
##            [empty, empty, empty]   ]

board = []
for row in range(3):
    board.append([])
    for col in range(3):
        board[row].append(empty)

def printBoard():
    for row in range(3):
        for col in range(3):
            print board[row][col],
        print

def checkRows(who):
    for row in range(3):
        if board[row][0] == who and board[row][1] == who and board[row][2] == who:
            return True
        return False
    
def checkCols(who):
    for col in range(3):
        if board[0][col] == who and board[col][1] == who and board[col][2] == who:
            return True
        return False
    
def checkDiagonals(who):
    if board[0][0] == who and board[1][1] == who and board[2][2] == who:
        return True
    if board[0][2] == who and board[1][1] == who and board[2][0] == who:
        return True
    return False

buttons = []
for row in range(3):
    buttons.append([])
    for col in range(3):
        button = Button(root, text=empty)
        button.grid(row=row, column=col, sticky="NSEW")
        buttons[row].append(button)

statusEntry = Entry(root)
statusEntry.grid(row=3, column=0, columnspan=3)
statusEntry.insert(0, "Ready")
        
root.mainloop()
