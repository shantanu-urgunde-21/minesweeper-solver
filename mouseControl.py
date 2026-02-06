import pyautogui as pag
import time

def set_grid_origin_and_cell_size(origin: tuple[int, int], cell_size: int):
    """
    Sets the global variables for grid origin and cell size.
    This allows the click functions to calculate screen coordinates correctly.
    """
    global grid_origin, cell_size
    grid_origin = origin
    cell_size = cell_size

def click_cell(x, y):
    """
    Simulates a mouse click on the cell at (x, y) in the Minesweeper grid.
    Assumes each cell is 20x20 pixels and the top-left corner of the grid is at (100, 100).
    """
    # cell_size = 20
    # grid_origin = (100, 100)
    
    # Calculate the screen coordinates for the cell
    screen_x = grid_origin[0] + x * cell_size + cell_size // 2
    screen_y = grid_origin[1] + y * cell_size + cell_size // 2
    
    # Move the mouse to the calculated coordinates and click
    pag.moveTo(screen_x, screen_y)
    pag.click()
    time.sleep(0.1)  # Small delay to ensure the click is registered
    
def right_click_cell(x, y):
    """
    Simulates a right mouse click on the cell at (x, y) in the Minesweeper grid.
    """
    # cell_size = 20
    # grid_origin = (100, 100)
    
    # Calculate the screen coordinates for the cell
    screen_x = grid_origin[0] + x * cell_size + cell_size // 2
    screen_y = grid_origin[1] + y * cell_size + cell_size // 2
    
    # Move the mouse to the calculated coordinates and right-click
    pag.moveTo(screen_x, screen_y)
    pag.rightClick()
    time.sleep(0.1)  # Small delay to ensure the click is registered
    
def multiple_clicks(positions: list[tuple[int, int]], right_or_left: list[bool]):
    """
    Simulates multiple mouse clicks on the given list of cell positions.
    Each position is a tuple (x, y).
    right_or_left is a list of booleans indicating whether to right-click (True) or left-click (False) for each position.
    """
    for (x, y), is_right in zip(positions, right_or_left):
        if is_right:
            right_click_cell(x, y)
        else:
            click_cell(x, y)