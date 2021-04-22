from tkinter import *
from game import Connect4
from constants import EMPTY, PLAYER_ONE, PLAYER_TWO, DRAW
from random_ai import RandomAI
from minimax_ai import MinimaxAI
from human import Human
import time

"""
This class represents the GUI of the game. This
makes the game more interactive rather than just
typing and such. We used the librrary tkinter for this
"""
class GUI:

    """
    Sets up the original board, grid, and allows 
    pieces to be placed by clicking
    """
    def __init__(self, master):
        self.master = master
        self.game_over = False
        self.player_1 = Human()
        self.player_2 = Human()
        self.temp1 = Human()
        self.temp2 = Human()
        self.curr_player = Human()
        self.game = Connect4(7,6)

        master.title('Connect Four')
        
        label = Label(master, text="Connect Four")
        label.grid(row=0)
        
        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.grid(row=2)

        self.draw_grid()

        self.canvas.bind('<Button-1>', self.canvas_click)
        self.drawButtons()

    """
    Whenever its clicked, it triggers this function.
    When the appropriate column is found, the function 
    uses that to make a move and approppriately finds a player
    """
    def canvas_click(self, event):
        # Dont continue if games over
        if self.game_over:
            return

        if not self.curr_player.human:
            return

        # Find column
        c = (event.x - 40) // 60
        
        game_over = EMPTY
        r = -1
        # If valid move
        if 0 <= c and c < self.game.width:
            # check if game over
            self.make_move(c)
            

    """
    This function makes the move for both the AI and the player.
    Both use it to return the move.
    """
    def make_move(self, move):
        # first have the game make the move and return whether the move was valid
        r = self.game.make_move(move)

        # if the move was valid draw the piece
        if r != -1:
            self.draw_piece(r,move)

        # check if the game is over and if so show the correct outcome
        if self.game.game_over:
            text = '' # Get the right text to draw
            self.game_over = True
            if self.game.game_over == DRAW:
                text = 'DRAW'
            if self.game.game_over == PLAYER_ONE:
                text = "PLAYER ONE WINS"
            if self.game.game_over == PLAYER_TWO:
                text = "PLAYER TWO WINS"
            self.canvas.create_text(250, 250, text=text, font=("Times New Roman", 32))
        else:
            # once the player makes a move the AIs (if applicable) will be prompted to make their 
            # move
            if self.curr_player == self.player_1:
                self.curr_player = self.player_2
                if not self.player_2.human:
                    self.master.update()
                    self.player_2.take_turn(self.game.board)
            elif self.curr_player == self.player_2:
                self.curr_player = self.player_1
                if not self.player_1.human:
                    self.master.update()
                    self.player_1.take_turn(self.game.board)

    """
    This function draws all the necesarry buttons needed for
    the game. This allows new game, and switching of players
    """
    def drawButtons(self):
        button = Button(self.master, text="New Game!", command=self.start_new_game)
        button.place(x=50,y=460)

        button = Button(self.master, text="Human", command=self.setHuman1)
        button.place(x=200,y=440)

        button = Button(self.master, text="Random AI", command=self.setRandomAI1)
        button.place(x=200,y=465)

        button = Button(self.master, text="Minimax AI", command=self.setMinimaxAI1)
        button.place(x=200,y=490)

        button = Button(self.master, text="Human", command=self.setHuman2)
        button.place(x=400,y=440)

        button = Button(self.master, text="Random AI", command=self.setRandomAI2)
        button.place(x=400,y=465)

        button = Button(self.master, text="Minimax AI", command=self.setMinimaxAI2)
        button.place(x=400,y=490)

        label = Label(self.master, text="Player 1")
        label.place(x=200,y=410)

        label = Label(self.master, text="Player 2")
        label.place(x=400,y=410)


    """
    This function starts the new game and does all the necessary
    things to set up the game.
    """
    def start_new_game(self):
        self.player_1 = self.temp1
        self.player_2 = self.temp2
        self.curr_player = self.player_1
        self.game = Connect4(7,6)
        self.canvas.delete(ALL)
        self.master.update()
        self.draw_grid()
        self.drawButtons()
        self.game_over = False
        if not self.player_1.human:
            self.player_1.take_turn(self.game.board)

    # Draws the grid
    # Maybe TODO: customizable size for board
    def draw_grid(self):
        for x in range(0, 8):
            self.canvas.create_line(40 + (x * 60), 20, 40 + (x * 60), 380)
        for y in range(0, 7):
            self.canvas.create_line(40, 20 + (y * 60), 460, 20 + (y * 60))

    # Draws the piece at the apprpriate location with the appropriate
    # color
    def draw_piece(self, y, x):
        color = None
        if self.game.turn == PLAYER_ONE:
            color = 'red'
        else:
            color = 'blue'

        self.canvas.create_oval(40 + (x*60), 20 + (y * 60), 100 + (x*60),80 + (y * 60) , fill=color)

    def setRandomAI1(self):
        self.temp1 = RandomAI(self)

    def setRandomAI2(self):
        self.temp2 = RandomAI(self)

    def setMinimaxAI1(self):
        self.temp1 = MinimaxAI(self, PLAYER_ONE)

    def setMinimaxAI2(self):
        self.temp2 = MinimaxAI(self, PLAYER_TWO)

    def setHuman1(self):
        self.temp1 = Human()

    def setHuman2(self):
        self.temp2 = Human()


root = Tk()
app = GUI(root)

root.mainloop() 