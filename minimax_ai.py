from constants import *
import numpy as np
import time
import random

"""
This AI represents an AI that will make a move using
the minimax algorithm. 
"""
class MinimaxAI:

    def __init__(self, game, gui, player):
        self.game = game
        self.gui = gui
        self.player = player

    """
    This is the move function that makes a move.
    The game calls this so that it can make a move.
    """
    def makeMove(self):
        validMoves = []
        for i,e  in enumerate(self.gui.game.board[0]):
            # get all the possible valid moves in the board
            if e == EMPTY:
                validMoves.append(i)

        time.sleep(.5)
        self.gui.makeMove(random.choice(validMoves))
    
    '''
    This is the heuristic function for the minimax algorithm. This function evaluates 
    how good the current board. The heuristic that I used is as follows: calculate the 
    difference between the number of possible open connect 4's. 
    '''
    def evaluate_board(self, board):
        p1_possible, p2_possible = 0,0

        # check all possible rows
        for row in board:
            p1_possible += self.count_possible(row, PLAYER_ONE)
            p2_possible += self.count_possible(row, PLAYER_TWO)

        # check all columns
        for i in range(len(board[0])):
            col = [x[i] for x in board]
            p1_possible += self.count_possible(col, PLAYER_ONE)
            p2_possible += self.count_possible(col, PLAYER_TWO)
        
        # check all possible diagnols going towards the top of the board starting from the leftmost column
        for i in range(len(board)):
            diag = self.get_diagnol(board, i, 0, True)
            p1_possible += self.count_possible(diag, PLAYER_ONE)
            p2_possible += self.count_possible(diag, PLAYER_TWO)

        #check all possible diagnols going towards the top of the board starting from the bottom row
        for i in range(1, len(board[0])):
            diag = self.get_diagnol(board, len(board) - 1, i, True)
            p1_possible += self.count_possible(diag, PLAYER_ONE)
            p2_possible += self.count_possible(diag, PLAYER_TWO)

        # check all possible diagnols going towards the bottom of the board starting from the top row
        for i in range(len(board[0])):
            diag = self.get_diagnol(board, 0, i, False)
            p1_possible += self.count_possible(diag, PLAYER_ONE)
            p2_possible += self.count_possible(diag, PLAYER_TWO)

        # check all possible diagnols going towards the bottom of the board starting from the leftmost column
        for i in range(1, len(board)):
            diag = self.get_diagnol(board, i, 0, False)
            p1_possible += self.count_possible(diag, PLAYER_ONE)
            p2_possible += self.count_possible(diag, PLAYER_TWO)

        print(p1_possible,p2_possible)

        return [p1_possible - p2_possible, p2_possible - p1_possible]
        
    def get_diagnol(self, board, start_row, start_col, upward):
        diag, curr_row, curr_col = [], start_row, start_col
        while curr_row >= 0 and curr_row < len(board) and curr_col >=0 and curr_col < len(board[0]):
            diag.append(board[curr_row][curr_col])
            curr_col += 1
            curr_row = curr_row - 1 if upward else curr_row + 1
        return diag

    def count_possible(self, arr, player):
        ret = 0
        for i in range(len(arr)):
            s = arr[i:i+4]
            if s.count(EMPTY) + s.count(player) == 4:
                ret += 1
        return ret

    def simulate_move(self, curr_board, col, player):
        copy = curr_board
        for i in range(len(curr_board), -1, -1):
            if curr_board[i]== EMPTY:
                copy[i][col] = player
        return copy




board = [[EMPTY for i in range(5)] for i in range(5)]
ai = MinimaxAI(None, None, None)

print(ai.evaluate_board(board))








