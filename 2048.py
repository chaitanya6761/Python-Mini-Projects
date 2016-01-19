"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    
    result = create_new_list(line) 
    count = 0    
    while count < len(result) :
        
        if(len(result) == 0 or len(result) == 1) :
            break
            
        if ( result[count] == result[count+1]) :
            result[count] = result[count] * 2
            result[count+1] = 0  
            count += 1
            
        count += 1
        
        if count + 1 >= len(result) :
            break
                                  
    result_merge = create_new_list(result)                                  
    return result_merge
    
                                  
def create_new_list(lst):  
    
    """
    Function that creates a new List.
    """
    
    result = [0 for element in range(len(lst))]
    count = 0
    for element in lst:
        if element != 0 :
            result[count] = element
            count += 1
                                  
    return result  

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
  
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self._tiles = {UP : [(0,col) for col in range(self._grid_width)],
                              DOWN : [(self._grid_height-1,col) for col in range(self._grid_width)],
                              LEFT : [(row,0) for row in range(self._grid_height)],
                              RIGHT : [(row,grid_width-1)for row in range(self._grid_height)] }
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [[ row*col*0 for col in range(self._grid_width)] for row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        offset = OFFSETS[direction]
        initial_tiles = self._tiles[direction]
        flag = 0
        
        for tile in initial_tiles:
            lst_of_tiles = [tile]
            lst_of_tiles_values = [self.get_tile(tile[0],tile[1])]
            
            step = 1
            while True:
                row  = tile[0] + step*offset[0]
                col  = tile[1] + step*offset[1]
                step += 1
                if row >= self._grid_height or row < 0 or col>=self._grid_width or  col < 0 :
                    break
                    
                
                lst_of_tiles.append((row,col))
                lst_of_tiles_values.append(self.get_tile(row,col))
                
            lst_of_tiles_values_new = merge(lst_of_tiles_values)
            
            count = 0
            
            for tile in lst_of_tiles:
                tile_value = lst_of_tiles_values_new[count]
                if(lst_of_tiles_values_new[count] != lst_of_tiles_values[count]):
                    flag += 1
                count += 1
                self.set_tile(tile[0],tile[1],tile_value)
        
        if flag > 0:
            self.new_tile()
        

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        lst_of_zero_tiles = []
        for row in range(self._grid_height) :
            for col in range(self._grid_width) :
                if self.get_tile(row,col) == 0 :
                    lst_of_zero_tiles.append([row,col])
                
        tile = random.choice(lst_of_zero_tiles)
        
        if random.random() < 0.9 : 
            self.set_tile(tile[0],tile[1],2)
        else :
            self.set_tile(tile[0],tile[1],4)
            
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value
        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
