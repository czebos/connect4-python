from constants import EMPTY, PLAYER_ONE, PLAYER_TWO
from game_over import CheckGameOver

"""
We chose to represent Connect 4 as a class, becase
there are a lot of variables that should be stored 
for a given game. It has the methods init, make_move
and and switchTurns.
"""
class Connect4:

    """
    This function just initiates all of the starting
    data for the Connect4 Game
    """
    def __init__(self, width, height):
        self.board = [[EMPTY for _ in range(width)] for _ in range(height)]
        self.turn = PLAYER_ONE
        self.width = width
        self.height = height

    """
    This function makes the move if its valid.
    It returns the winner if there is one and the row.
    """
    def make_move(self, col):
        if col < 0 or col >= self.width:
            print("Not a valid move")
            return [EMPTY, -1]
        else:
            # If col filled up
            if self.board[0][col] != EMPTY:
                print("Not a valid move")
                return [EMPTY, -1]
            # Find the first time a slot is open
            top = 0
            while top < self.height and self.board[top][col] == EMPTY:
                top += 1
            top -= 1
            self.board[top][col] = self.turn
            self.switchTurns()
            return [CheckGameOver(self.board), top]

    """
    This function switches the current players move.
    """
    def switchTurns(self):
        if self.turn == PLAYER_ONE:
            self.turn = PLAYER_TWO
        else:
            self.turn = PLAYER_ONE

