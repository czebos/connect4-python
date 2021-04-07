from constants import EMPTY, PLAYER_ONE, PLAYER_TWO, DRAW

"""
This checks if there is a current winner for the game
board and returns it.
"""
def CheckGameOver(board):
    for i in range(len(board)): # for each space
        for j in range(len(board[0])):
            winner = CheckDirections(board,i,j) # check if theres 4 in a row in any direciton
            if winner != EMPTY:
                return winner
    for i in range(len(board)): # for each space
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                return EMPTY
    return DRAW

"""
This function returns the winner if there is one.
It takes in a board, and a given x,y representing
a space. It then checked every direction from that 
space for a connect 4.
"""
def CheckDirections(board, x, y):
    color = board[x][y]
    # No winner
    if color == EMPTY:
        return EMPTY
    dir = [-1,0,1]
    # check every direction, up, left right down and combinations of them
    for i in dir:
        for j in dir:
            currX = x
            currY = y
            count = 0
            if i == 0 and j == 0:
                continue
            # if its the same piece as before, and in bounds, keep going that direction.
            while currX >= 0 and currX < len(board) and currY >=0 and currY < len(board[1]) and board[currX][currY] == color:
                count += 1
                currX += i
                currY += j
            # if thers a connect4
            if count >= 4:
                return color

    return EMPTY
