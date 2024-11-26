from Cusarray import CustomArray
class Array2d:
    def __init__(self, nrows, ncols):
        self.nrows = CustomArray(nrows)
        for i in range(nrows):
            self.nrows[i] = CustomArray(ncols)

    def numRows(self):
        return len(self.nrows)

    def numcolumns(self):
        return len(self.nrows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            for j in range(self.numcolumns()):
                self.nrows[row][j] = value

    def __getitem__(self, ntuple):
        assert len(ntuple) == 2, "invalid range"
        row = ntuple[0]
        col = ntuple[1]
        assert 0 <= row < self.numRows() and 0 <= col < self.numcolumns(), "index out of range"
        thearray = self.nrows[row]
        return thearray[col]

    def __setitem__(self, ntuple, value):
        assert len(ntuple) == 2, "invalid range"
        row = ntuple[0]
        col = ntuple[1]
        assert 0 <= row < self.numRows() and 0 <= col < self.numcolumns(), "index out of range"
        self.nrows[row][col] = value