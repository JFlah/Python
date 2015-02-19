# 3 23 14 Sudoku exmaple

# SOLVE ALGORITHM GUIDELINES ON BBV

def put(row, col, val):
    global board
    board[row][col].delete(0,END)
    fields[row][col].insert(0, val)

    to help with solving, can do put(row, col, x)

def solve():
    find empty cell:
        make guesses 1-9 till we find one with no conflict
        no conflicts:
            call solve():

    if no empty cells:
        return True


    should return true or false on whether or not it was able to solve board



row 4 col 5 is empty
guess 1:
    conflicts? Y
guess 2:
    conflicts? N
    call solve recursively()
    if solve returns false,
    keep guessing
guess 3,4,5,6, all failed
guess 7:
    call solve recusrively


Solve algorithm (returns true if successful, false if not)
1)scan all rows and columns, find empty cell...
this invocation of solve.. (will only examine that one cell)

2) Try all possible guesses .. which is 1-9 
	for each guess, see if that guess is
	consistent ( no row, col or cluster conflicts):
            No: keep guessing
            yes: may have found part of solution, lets find out):
                recursively call solve:
                    if solve returns true, return True (board solved)
                    if solve returns false, keep guessing

        set current cell to Empty
        return False
3) if scan (step 1) failed to find empty cell, board is solved, return True
	

    
