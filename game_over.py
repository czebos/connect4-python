from constants import EMPTY, PLAYER_ONE, PLAYER_TWO

def CheckGameOver(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            winner = CheckDirections(board,i,j) 
            if winner != EMPTY:
                return winner
    return EMPTY


def CheckDirections(board, x, y):
    color = board[x][y]
    if color == EMPTY:
        return EMPTY
    dir = [-1,0,1]
    for i in dir:
        for j in dir:
            currX = x
            currY = y
            count = 0
            if i == 0 and j == 0:
                continue
            while currX >= 0 and currX < len(board) and currY >=0 and currY < len(board[1]) and board[currX][currY] == color:
                count += 1
                currX += i
                currY += j
            if count >= 4:
                return color

    return EMPTY

def printBoard(board):
    for i in board:
        string = ""
        for j in i:
            string += str(j)
        print(string)

board = [[1,0,0,0,0], [1,1,0,1,1], [1,0,0,0,0], [1,1,0,1,1], [2,2,0,2,2]]
printBoard(board)
print(CheckGameOver(board))
