# More list stuff 2/24/14

#a = [[1,2,82],[99,88],"hi"]

#list-ception ^

#a[row][column]

#print a[0][2]
#print a[0]
#print a[1]


#a = [
 #  [3,12,22],
  #  [2,99,16],
   # [12,-1,402

# Tic Tac Toe

X = "X"
O = "O"
empty = "."

##board = [   [empty, empty, empty],
##            [empty, empty, empty],
##            [empty, empty, empty]   ]

board = []

def printBoard():
    for row in range(3):
        for col in range(3):
            print board[row][col],
        print

def play():
    turn = X
    while True:
        row = int(raw_input(turn + ", what row? "))
        col = int(raw_input(turn + ", what col? "))
        if board[row][col] != empty:
            print turn, "is a cheater!"
            print turn, "LOSES"
            print
            return
        board[row][col] = turn
        printBoard()
        if checkRows(turn) or checkCols(turn) or checkDiagonals(turn):
            print turn, "WINS!"
            return
        
        # Now change turns
        if turn == X:
            turn = O
        else:
            turn = X

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
    if board[0][2] == who and board [1][1] == who and board[2][0] == who:
        return True
    return False
        

play()
