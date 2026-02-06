class Grid:
    def __init__(self, grid: list[list[int]] = None, height: int = None, width: int = None):
        """
        Initialize with an existing grid OR with dimensions to create a blank one.
        """
        if grid is not None:
            self.grid = grid
            self.height = len(grid)
            self.width = len(grid[0]) if self.height > 0 else 0
        elif height is not None and width is not None:
            # Create a blank grid filled with 0s
            self.grid = [[0 for _ in range(width)] for _ in range(height)]
            self.height = height
            self.width = width
        else:
            # Default empty
            self.grid = []
            self.height = 0
            self.width = 0

    def __getitem__(self, position):
        """
        Allows accessing grid via grid[row, col]
        """
        row, col = position
        return self.grid[row][col]

    def __setitem__(self, position, value):
        """
        Allows setting grid via grid[row, col] = value
        """
        row, col = position
        self.grid[row][col] = value
        
    def update_multiple(self, positions: list[tuple], values: list[int]):
        """
        Updates multiple cells at once.
        """
        for i, (row, col) in enumerate(positions):
            self.grid[row][col] = values[i]

    def __str__(self):
        """
        Helper to print the grid in a readable format.
        """
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])
    

class Image:
    def __init__(self, path: str):
        self.path = path