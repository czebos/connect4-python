from constants import EMPTY
import random

class RandomAI:

    def __init__(self, game, gui):
        self.game = game
        self.gui = gui

    def makeMove(self):
        validMoves = []
        for i,e  in enumerate(self.gui.game.board[0]):
            print((i,e))
            if e == EMPTY:
                validMoves.append(i)

        print(validMoves)
        self.gui.makeMove(random.choice(validMoves))
