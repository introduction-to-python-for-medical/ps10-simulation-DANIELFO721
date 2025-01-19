import copy


def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)  # Define grid size dynamically
    update_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # Tree present
                # Safely check neighbors
                neighbors = []
                if i > 0:  # Above
                    neighbors.append(grid[i-1][j])
                if i < grid_size - 1:  # Below
                    neighbors.append(grid[i+1][j])
                if j > 0:  # Left
                    neighbors.append(grid[i][j-1])
                if j < grid_size - 1:  # Right
                    neighbors.append(grid[i][j+1])
                
                # If any neighbor is on fire, the tree catches fire
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
