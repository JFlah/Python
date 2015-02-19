# Tic Tac Toe
# GUI version

from Tkinter import *
root = Tk()
root.title("Tic Tac Toe")


X = 'X'
O = 'O'
EMPTY = '.'
GAMEOVER = 'NOOOO!!'
turn = X

##board = [  [EMPTY, EMPTY, EMPTY],
##           [EMPTY, EMPTY, EMPTY],
##           [EMPTY, EMPTY, EMPTY]   ]

board = [ ]
for row in range(3):
    board.append( [ ] )
    for col in range(3):
        board[row].append(EMPTY)


def printBoard():
    for row in range(3):
        for col in range(3):
            print board[row][col],
        print

# returns True if 'who' has filled any row
# return False otherwise
def checkRows(who):
    for row in range(3):
        if board[row][0]==who and board[row][1]==who and board[row][2]==who:
            return True
    return False

def checkCols(who):
    for col in range(3):
        if board[0][col]==who and board[1][col]==who and board[2][col]==who:
            return True
    return False

def checkDiagonals(who):
    if board[0][0]==who and board[1][1]==who and board[2][2]==who:
        return True
    if board[0][2]==who and board[1][1]==who and board[2][0]==who:
        return True
    return False

# return True or False, depending on whether 'who' won the game
def checkWin(who):
    if checkRows(who) or checkCols(who) or checkDiagonals(who):
        return True
    else:
        return False

def buttonPressed(row, col):
    global turn, buttons
    if turn==GAMEOVER:
        return
    print "Button pressed, row is", row, ", col is", col
    if board[row][col] != EMPTY:
        statusEntry.delete(0, END)
        statusEntry.insert(0, turn + " Cheated!")
        return
    board[row][col] = turn
    buttons[row][col].config(text=turn)
    if checkWin(turn):
        statusEntry.delete(0, END)
        statusEntry.insert(0, turn + ", WINS!!")
        turn = GAMEOVER
        return
    if turn==X:
        turn = O
    else:
        turn = X

# create buttons
buttons = [ ]
for row in range(3):
    buttons.append( [ ] )
    for col in range(3):
        def click(r=row, c=col): # will use row, col at FUNCTION DEFINITION time, not function execution time
            buttonPressed(r, c)
            
        button = Button(root, text=EMPTY, command=click)
        button.grid(row=row, column=col, sticky="NSEW")
        buttons[row].append(button)

statusEntry = Entry(root)
statusEntry.grid(row=3, column=0, columnspan=3)
statusEntry.insert(0, "Ready")






root.mainloop()
