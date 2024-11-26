import ctypes

class CustomArray:
    """A simple 1D array implementation using ctypes."""
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        self._elements = (ctypes.py_object * size)()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert 0 <= index < self._size, "Array index out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < self._size, "Array index out of range"
        self._elements[index] = value

    def clear(self, value):
        for i in range(self._size):
            self._elements[i] = value

    def __iter__(self):
        return Arrayiterator(self._elements)


class Arrayiterator:

    def __init__(self, theArray):
        self.arrayref = theArray
        self.nxt = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.nxt < len(self.arrayref):
            entry = self.arrayref[self.nxt]
            self.nxt += 1
            return entry
        else:
            raise StopIteration