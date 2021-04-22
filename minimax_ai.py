from constants import *
import numpy as np
import time
import random
import copy

"""
This AI represents an AI that will make a move using
the minimax algorithm. 
"""
class MinimaxAI:

    def __init__(self, gui, player):
        self.gui = gui
        self.player = player
        self.human = False

    """
    This is the move function that makes a move.
    The game calls this so that it can make a move.
    """
    def take_turn(self, board):
        # pause for more fluid game visuals
        time.sleep(.2)
        # calcualte the best move using minimax
        best_move = self.minimax(board,2)
        self.gui.make_move(best_move)

    '''
    This is the minimax algorithm. The algorithm has two components, minimizing and 
    maximizing. The maximizing portion of the algorithm serves to maximize ones own score,
    while the minimizing portion serves to minimize the score the opposing player can
    can achieve.
    '''
    def minimax(self, board, cutoff):
        valid_moves = self.get_valid_moves(board)
        best_move = valid_moves[0]
        best_val = float('-inf')
        next_player = PLAYER_ONE if self.player == PLAYER_TWO else PLAYER_TWO
        for move in valid_moves:
            next_state = self.simulate_move(board, move, self.player) 
            next_state_val = self.minimizer(next_state, cutoff-1, next_player)
            if next_state_val > best_val:
                best_val = next_state_val
                best_move = move
        return best_move

    '''
    This is the maximizer, used to maximize the score that the player can achieve
    '''
    def maximizer(self, board, cutoff, curr_player):
        board_state = self.evaluate_board(board)
        if cutoff == 0 or self.is_terminal(board_state):
            return board_state[self.player-1]
        next_player = PLAYER_ONE if self.player == PLAYER_TWO else PLAYER_TWO
        v = float('-inf')
        valid_moves = self.get_valid_moves(board)
        for move in valid_moves:
            next_state = self.simulate_move(board, move, curr_player) 
            next_state_val = self.minimizer(next_state, cutoff-1, next_player)
            v = max(v, next_state_val)
        return v

    '''
    This is the minimizer, this serves to minimize the possible score the opponent can
    achieve
    '''
    def minimizer(self, board, cutoff, curr_player):
        board_state = self.evaluate_board(board)
        if cutoff == 0 or self.is_terminal(board_state):
            return board_state[self.opposing_player(self.player)-1]
        next_player = PLAYER_ONE if self.player == PLAYER_TWO else PLAYER_TWO
        v = float('inf')
        valid_moves = self.get_valid_moves(board)
        for move in valid_moves:
            next_state = self.simulate_move(board, move, curr_player) 
            next_state_val = self.maximizer(next_state, cutoff-1, next_player)
            v = min(v, next_state_val)
        return v

    '''
    This is the heuristic function for the minimax algorithm. This function evaluates 
    how good the current board. The heuristic that I used is as follows: calculate the 
    difference between the number of possible open connect 4's. 
    '''
    def evaluate_board(self, board):
        p1_score = 0
        p2_score = 0
        if self.check_draw(board):
            return [0, 0]

        # check all possible rows
        for row in board:
            p1_score += self.score_slice(row, PLAYER_ONE)
            p2_score += self.score_slice(row, PLAYER_TWO)
            winner, res = self.check_winner(row)
            if winner:
                return res

        # check all columns
        for i in range(len(board[0])):
            col = [x[i] for x in board]
            p1_score += self.score_slice(col, PLAYER_ONE)
            p2_score += self.score_slice(col, PLAYER_TWO)
            winner, res = self.check_winner(col)
            if winner:
                return res
        
        # check all possible diagnols going towards the top of the board starting from the leftmost column
        for i in range(len(board)):
            diag = self.get_diagnol(board, i, 0, True)
            p1_score += self.score_slice(diag, PLAYER_ONE)
            p2_score += self.score_slice(diag, PLAYER_TWO)
            winner, res = self.check_winner(diag)
            if winner:
                return res

        #check all possible diagnols going towards the top of the board starting from the bottom row
        for i in range(1, len(board[0])):
            diag = self.get_diagnol(board, len(board) - 1, i, True)
            p1_score += self.score_slice(diag, PLAYER_ONE)
            p2_score += self.score_slice(diag, PLAYER_TWO)
            winner, res = self.check_winner(diag)
            if winner:
                return res

        # check all possible diagnols going towards the bottom of the board starting from the top row
        for i in range(len(board[0])):
            diag = self.get_diagnol(board, 0, i, False)
            p1_score += self.score_slice(diag, PLAYER_ONE)
            p2_score += self.score_slice(diag, PLAYER_TWO)
            winner, res = self.check_winner(diag)
            if winner:
                return res

        # check all possible diagnols going towards the bottom of the board starting from the leftmost column
        for i in range(1, len(board)):
            diag = self.get_diagnol(board, i, 0, False)
            p1_score += self.score_slice(diag, PLAYER_ONE)
            p2_score += self.score_slice(diag, PLAYER_TWO)
            winner, res = self.check_winner(diag)
            if winner:
                return res

        return [p1_score, p2_score]
        
    def get_diagnol(self, board, start_row, start_col, upward):
        diag, curr_row, curr_col = [], start_row, start_col
        while curr_row >= 0 and curr_row < len(board) and curr_col >=0 and curr_col < len(board[0]):
            diag.append(board[curr_row][curr_col])
            curr_col += 1
            curr_row = curr_row - 1 if upward else curr_row + 1
        return diag

    
    '''
    This function scores a particular row/col/diagnol. Points are awarded based on how many in the row the player
    can get, and points are subtracted for the opponent having more in a row
    '''
    def score_slice(self, arr, player):
        for i in range(len(arr)):
            s = arr[i:i+4]
            if len(s) == 4:
                if s.count(player) == 4:
                    return float('inf')
                if s.count(player) == 3 and s.count(EMPTY) == 1:
                    return 5
                if s.count(player) == 2 and s.count(EMPTY) == 2:
                    return 2
                if s.count(self.opposing_player(player)) == 3 and s.count(EMPTY) == 1:
                    return -100

        return 0

    '''
    checks to see if anyone won. returns a score for each player depending on who won or lost
    '''

    def check_winner(self, arr):
        for i in range(len(arr)):
            s = arr[i:i+4]
            if s.count(PLAYER_ONE) == 4:
                return True, [float('inf'), float('-inf')]
            if s.count(PLAYER_TWO) == 4:
                return True, [float('inf'), float('-inf')]
        return False, [0,0]

    '''
    gets valid moves on the board
    '''
    
    def get_valid_moves(self, board):
        moves = []
        for i in range(len(board[0])):
            if board[0][i] == EMPTY:
                moves.append(i)
        return moves

    '''
    checks if there's a draw on the board
    '''
    def check_draw(self, board):
        for row in board:
            for val in row:
                if val == EMPTY:
                    return False
        return True

    '''
    checks if a board state is terminal (win,loss,draw)
    '''
    def is_terminal(self, arr):
        return (arr == [float('inf'), float('-inf')] or arr == [float('-inf'),float('inf')] or arr == [0, 0])

    '''
    simulates a move on the board and returns the board after the theoretical move. used for scoring 
    purposes
    '''
    def simulate_move(self, curr_board, col, player):
        c = copy.deepcopy(curr_board)
        for i in range(len(curr_board)-1, -1, -1):
            if curr_board[i][col] == EMPTY:
                c[i][col] = player
                break
        return c

    def opposing_player(self, player):
        if player == PLAYER_ONE:
            return PLAYER_TWO
        return PLAYER_ONE