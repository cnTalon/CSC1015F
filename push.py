# move the values inside the grid around
# 24 April 2022

import util

def push_up(grid):
    """merge grid values upwards"""
    newGrid = []
    newGrid = util.create_grid(newGrid)     # sets new grid for game
    while grid != newGrid:
        newGrid = util.copy_grid(grid)      # copies the computer given grid as new grid
        for row in range(3):
            for col in range(4):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row+1][col]   # replaces 0 with value of the above row
                    grid[row+1][col] = 0  
    for row in range(3):
        for col in range(4):
            if grid[row][col] == grid[row+1][col]:   # combines values if they are equal
                grid[row][col] = grid[row][col] + grid[row+1][col]  # adds two equal values
                grid[row+1][col] = 0    # sets the previous row to 0
            if grid[row][col] == 0:
                grid[row][col] = grid[row+1][col]   # sets 0 to value in above row
                grid[row+1][col] = 0    # sets below row 0
    return grid

def push_down(grid):
    """merge grid values downwards"""
    newGrid = []
    newGrid = util.create_grid(newGrid)     # sets new grid
    while grid != newGrid:
        newGrid = util.copy_grid(grid)      # copies computer given grid as new grid
        for row in range(3,0,-1):
            for col in range(4):
                if grid[row][col] == 0:
                    grid[row][col] = grid[row-1][col]   # replaces 0 with value of row below
                    grid[row-1][col] = 0    
    for row in range(3,0,-1):
        for col in range(4):
            if grid[row][col] == grid[row-1][col]:  # combines values if they are equal
                grid[row][col] = grid[row][col] + grid[row-1][col]  # adds equal values
                grid[row-1][col] = 0
            if grid[row][col] == 0:
                grid[row][col] = grid[row-1][col]   # sets 0 to value of previous row
                grid[row-1][col]=0
    return grid

def push_left(grid):
    """merge grid values left"""
    for row in range(4):    # push out zeros
        eachRow =[]
        for col in range(4):
            if grid[row][col] != 0:
                eachRow.append(grid[row][col])
        for col in range(4):
            if col >= len(eachRow):
                grid[row][col] = 0
            else:
                grid[row][col] = eachRow[col]
    for row in range(4):    # combine equal values
        for col in range(3):
            if grid[row][col] == grid[row][col+1]:
                grid[row][col] *= 2
                grid[row][col+1] = 0
    for row in range(4):    # push into correct spot
        eachRow=[]
        for col in range(4):
            if grid[row][col] != 0:
                eachRow.append(grid[row][col])
        for col in range(4):
            if col >= len(eachRow):
                grid[row][col] = 0
            else:
                grid[row][col] = eachRow[col]
                
def push_right(grid):
    """merge grid values right"""
    for row in range(4):    # push out zeros
        eachRow = []
        for col in range(-1,-5,-1):
            if grid[row][col] != 0:
                eachRow.append(grid[row][col])
        eachRow.reverse()
        for col in range(-1,-5,-1):
            if col <= len(eachRow) * -1 - 1:
                grid[row][col] = 0
            else:
                grid[row][col] = eachRow[col]
    for row in range(4):    # combine equal values
        for col in range(-1,-4,-1):
            if grid[row][col] == grid[row][col-1]:
                grid[row][col] *= 2
                grid[row][col-1] = 0
    for row in range(4):    # push to correct spot
        eachRow = []
        for col in range(-1,-5,-1):
            if grid[row][col] != 0:
                eachRow.append(grid[row][col])
        eachRow.reverse()
        for col in range(-1,-5,-1):
            if col <= len(eachRow) * -1 - 1:
                grid[row][col] = 0
            else:
                grid[row][col] = eachRow[col]