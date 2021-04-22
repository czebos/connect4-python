from constants import EMPTY
import time
import random

"""
This AI represents an AI that will make a random move.
When given a choice, it will find all of the possible
move and make a random one amonst them
"""
class RandomAI:

    def __init__(self, gui):
        self.gui = gui
        self.human = False

    """
    This is the move function that makes a move.
    The game calls this so that it can make a move.
    """
    def take_turn(self, board):
        time.sleep(.2)
        validMoves = []
        for i in range(len(board[0])):
            if board[0][i] == EMPTY:
                validMoves.append(i)
        move = random.choice(validMoves)
        self.gui.make_move(move)
