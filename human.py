'''
This class serves to represent a player that is human. The class is primarily used 
for identification purposes so the game knows to wait for inputs
'''
class Human:
    def __init__(self):
        self.human = True
    '''
    Humans take turns on their own accord by clicking the board so this function doesn't need to 
    do anything 
    '''
    def take_turn(self, board):
        return