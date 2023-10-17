from .constants import *
from .ship import *

class User:
    
    def __init__ (self, board):
        self.board = board
        self.ships = []
        
          
    def get_board(self):
        return self.board
    
    def hit(self, row, col, cell):
      pass
        
    
    def put_ship(self, coords, win):
        """ This is the principal method to put the ships and manages all of the classes similar methods"""
        temp_cells = []
        # coords = set of tuples with the rows and cols of the selected cells to be ships 
        for (row, col) in coords:
           temp_cells.append(self.board.get_cell(row, col))
        
        ship = Ship(temp_cells) #Creates the ship
        self.board.draw_ship(win, ship) # draws it in the user board
        self.ships.append(ship) #Stores all the user ships 
       
        return ship
    

        
        
        
    