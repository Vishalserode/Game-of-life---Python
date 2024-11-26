from array2 import Array2d

class LifeGrid:
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, numRows, numCols):
        self.grid = Array2d(numRows, numCols)
        self.configure(list())

    def numberRows(self):
        return self.grid.numRows()

    def numberCols(self):
        return self.grid.numcolumns()

    def configure(self, coordlist):
        for i in range(self.numberRows()):
            for j in range(self.numberCols()):
                self.clearcell(i, j)

        for coord in coordlist:
            self.setcell(coord[0], coord[1])

    def islivecell(self, row, col):
        return self.grid[row, col] == self.LIVE_CELL

    def clearcell(self, row, col):
        self.grid[row, col] = self.DEAD_CELL

    def setcell(self, row, col):
        self.grid[row, col] = self.LIVE_CELL

    def numliveneighbors(self, row, col):
        count =0
        direction = [
            (-1,-1),(-1,0),(-1,1),
            (0,-1),        (0,1),
            (1,-1),(1,0),(1,1)
        ]
        for dr,di in direction:
            neighbour_row = row + dr
            neighbour_col = col + di

            if 0 <= neighbour_row < self.numberRows() and 0 <= neighbour_col < self.numberCols():
                if self.islivecell(neighbour_row, neighbour_col):
                    count += 1
        return count