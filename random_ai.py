from constants import EMPTY
import time
import random

"""
This AI represents an AI that will make a random move.
When given a choice, it will find all of the possible
move and make a random one amonst them
"""
class RandomAI:

    def __init__(self, game, gui):
        self.game = game
        self.gui = gui

    """
    This is the move function that makes a move.
    The game calls this so that it can make a move.
    """
    def makeMove(self):
        validMoves = []
        for i,e  in enumerate(self.gui.game.board[0]):
            print((i,e))
            
            if e == EMPTY:
                validMoves.append(i)

        time.sleep(.5)
        self.gui.makeMove(random.choice(validMoves))
