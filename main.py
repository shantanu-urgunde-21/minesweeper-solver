import imageToList
from schemas import Grid
import mouseControl


if __name__ == "__main__":
    grid_data = imageToList.image_to_grid("minesweeper_image.png")
    grid = Grid(grid=grid_data)
    print(grid)