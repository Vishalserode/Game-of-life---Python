from life import LifeGrid
import time

INIT_CONFIG = [(1,1), (1,2), (2,2), (3,2)]

WIDTH = 10
HEIGHT = 10
NUM_GEN = 10

def main():
    grid = LifeGrid(WIDTH, HEIGHT)
    grid.configure(INIT_CONFIG)

    draw(grid)

    for i in range(NUM_GEN):
        evolve(grid)
        draw(grid)

def evolve(grid):
    liveCells = list()

    for i in range(grid.numberRows()):
        for j in range(grid.numberCols()):
            neighbors = grid.numliveneighbors(i, j)

            if (neighbors == 2 and grid.islivecell(i,j)) or neighbors == 3:
                liveCells.append((i,j))
    grid.configure(liveCells)
def draw(grid):
    result = ""
    for i in range(grid.numberRows()):
        for j in range(grid.numberCols()):
            if grid.islivecell(i, j):
                result += "@ "
            else:
                result += ". "
        result += "\n"
    print(result)


main()
