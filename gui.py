from tkinter import *
from game import Connect4
from constants import EMPTY, PLAYER_ONE, PLAYER_TWO, DRAW

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
        self.game = Connect4(7,6)
        self.game_over = False

        master.title('Connect Four')
        
        label = Label(master, text="Connect Four")
        label.grid(row=0)
        
        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.grid(row=2)

        self.draw_grid()

        self.canvas.bind('<Button-1>', self.canvas_click)

    """
    Whenever its clicked, it triggers this function.
    When the appropriate column is found, the function 
    uses that to make a move and approppriately finds a player
    """
    def canvas_click(self, event):
        # Dont continue if games over
        if self.game_over:
            return

        # Find column
        c = (event.x - 40) // 60
        
        game_over = EMPTY
        r = -1
        # If valid move
        if 0 <= c and c < self.game.width:
            # check if game over
            game_over, r = self.game.makeMove(c)
            if game_over:
                text = '' # Get the right text to draw
                self.game_over = True
                if game_over == DRAW:
                    text = 'DRAW'
                if game_over == PLAYER_ONE:
                    text = "PLAYER ONE WINS"
                if game_over == PLAYER_TWO:
                    text = "PLAYER TWO WINS"
                self.canvas.create_text(250, 450, text=text, font=("Times New Roman", 32))
            # if valid move
            if r != -1:
                self.draw_piece(r,c)





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

root = Tk()
app = GUI(root)

root.mainloop()