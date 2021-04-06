from constants import EMPTY, PLAYER_ONE, PLAYER_TWO
from game import Connect4


def printBoard(board):
    for i in board:
        string = ""
        for j in i:
            string += str(j)
        print(string)

game = Connect4(7,6)
printBoard(game.board)
end = 0
while True:
    move = int(input())
    end = game.makeMove(move)
    printBoard(game.board)
    if end != 0:
        break

print(str(end) + " is the winner!")

    
