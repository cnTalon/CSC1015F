# utility for manipulating 2d arrays
# 19 April 2022

import copy

def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+" + "-"*20 + "+")   # prints the top of the box
    for row in range(4):
        eachRow = "|"           # adds the | for the left side of the box
        for col in range(4):
            if grid[row][col] != 0:
                # creates each row of the grid
                eachRow += str(grid[row][col]) + ' '*(5 - len(str(grid[row][col])))
            else:
                eachRow += ' '*5    # adds empty spaces for where it is 0
        print(eachRow + '|')
    print("+" + "-"*20 + "+")   # prints the bottom of the box

def check_lost(grid):
    """return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""
    outcome = True
    for row in range(4):
        for num in range(4):
            if grid[row][num] == 0: # if theres a 0 anywhere False is returned
                outcome = False
            else:
                if not num==3: 
                    if grid[row][num] == grid[row][num+1]:  # compares adjacent values per column
                        outcome = False
                if not row==3:
                    if grid[row][num] == grid[row+1][num]:  # compares adjacent values for each row
                        outcome = False
    return outcome

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(4):
        for col in range(4):
            if grid[row][col] >= 32:    # checks every number in grid
                return True
    return False

def copy_grid(grid):
    """return a copy of the given grid"""
    origrid = copy.deepcopy(grid)       # saves a copy of the original grid
    return origrid

def grid_equal(grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    outcome = True
    if grid1 == grid2:
        outcome = True
    else:
        outcome = outcome and False
    return outcome
