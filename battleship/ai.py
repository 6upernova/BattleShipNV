"""
The AI class represents the AI opponent in the game.
It's responsible for generating its own game board and placing its ships randomly.

The AI will make decisions on where to guess based on the information provided in the sentences and its strategies.

"""
from .constants import *
from .ship import *
import random

class Ai:
    """
    Represents a ship object in the game.
    """

    # Define a class-level variable to hold the AI modes
    POSSIBLE_MODES = ["Target", "Hunt"]

    def __init__ (self, board, user):
        """
        Constructor for the AI class.
        """

        self.board = board
        self.ships = []
        self.opponent = user
        self.moves_made = set()
        self.mode = Ai.POSSIBLE_MODES[0]

        # List of potential targets
        self.knowledge = set()
        
    
    def get_board(self):
        return self.board
    

    def ask_if_hit(self, row, col):
        """
        Returns true if the cell passed as a parameter contains a ship
        """     
        return self.board.get_cell(row, col).is_ship


    def generate_coords(self, length):
        """
        Generates a random set of coordinates, ensuring they are consecutive and do not contain a ship.
        """

        while True:
            # Determine the direction (horizontal or vertical) randomly.
            orientation = random.choice(['vertical', 'horizontal'])

            # Randomly select the starting position.
            if orientation == 'horizontal':
                start_row = random.randint(0, 9 - 1)
                start_col = random.randint(0, 9 - length)
            else:
                start_row = random.randint(0, 9 - length)
                start_col = random.randint(0, 9 - 1)

            # Generate consecutive coordinates based on the chosen direction.
            coords = []
            for i in range(length):
                if orientation == 'horizontal':
                    coords.append((start_row, start_col + i))
                else:
                    coords.append((start_row + i, start_col))

            # Check if the generated coordinates contain any cells with ships.
            has_ship = any(self.board.get_cell(row, col).is_ship() for row, col in coords)

            # If there are no ships in the generated coordinates, return them.
            if not has_ship:
                return coords


    def place_ship(self, win, length):
        """
        Places AI ship on the game board using coordinates generated by generate_coords.
        """

        coords = self.generate_coords(length)

        temp_cells = []
        for (row, col) in coords:
            temp_cells.append(self.board.get_cell(row, col))

        ship = Ship(temp_cells)  # Creates the ship
        self.board.draw_ship(win, ship)
        self.ships.append(ship)  # Stores all the AI ships
        self.board.update_board()
        
        return ship


    def hunt(self):
        """
        In Hunt mode the AI will shoot at random coordinates with even parity
        (later on the hunt mode will take into account the pdf_value of each cell,
        so it can redirect the movements to cells with the highest chance of having a ship)
        """

        # Generate random coordinates with even parity
        row = random.randint(0, 9)
        col = random.randint(0, 9)

        if (row + col) % 2 == 0:
            # Check if the cell contains a ship part
            hit = opponent.ask_if_hit(row, col)
            
            # Store cell coords in a tuple
            cell = row, col

            return hit, cell


    def make_guess(self, board, sentence):
        """
        Makes a guess: at first the AI will start in 'Hunt' mode. 
        Once a ship is touched, the inferences will be put into the sentence and the AI ​​will enter 'target' mode
        """

        # if there is no knowledge about possible targets, enter 'Hunt' mode
        if not self.knowledge:
            is_a_hit, cell = self.hunt()
        else:

        # If the guess hit a ship, add new knowledge
        if is_a_hit:
            # Construct a new Sentence object and update knowledge
            new_knowledge = Sentence(cell)

            for cell in new_knowledge:
                self.knowledge.add(cell) 


