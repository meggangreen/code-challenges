""" n Queens """

from collections import deque
from copy import deepcopy

class Queen(object):

    def __init__(self, row):
        self.row = row
        self.col = None
        self.possibles = deque()


    def __repr__(self):
        return '<Queen ({}, {}) >'.format(self.row, self.col)


    def get_possibles(self, grid):
        """ Get list of possible coordinates. """

        for i in range(grid.bounds):
            if grid.layout[self.row][i] == 1:
                self.possibles.append(i)


class Grid(object):

    def __init__(self, n, layout=None):
        self.bounds = n
        self.layout = layout if layout else [[1 for i in range(n)] for j in range(n)]


    def __repr__(self):
        return '<Grid n={} {}>'.format(self.bounds, self.layout)


    def update_squares(self, queen):
        """ Sets Qs and 0s according to past in coordinates. """

        row, col = queen.row, queen.col
        self.layout[row] = [0] * self.bounds
        self.layout[row][col] = 'Q'

        for d in range(1, self.bounds):
            # Set rows and cols to limit if statements
            all_coords = [(row+d, col-d), (row+d, col), (row+d, col+d)]

            # Set possible coordinates, ignoring out-of-bounds, Qs, and 0s
            for (i, j) in all_coords:
                if ( queen.row <= i < self.bounds and 0 <= j < self.bounds and
                                                      self.layout[i][j] == 1 ):
                    self.layout[i][j] = 0


def do_place_queen(grid, row, queens):
    """ Place one Queen in the grid; recursively call down. If Queen cannot be
        placed, return False and back track. If successive Queen cannot be
        placed, try next possible coordinate. If no possible coordinates remain,
        return False and back track.

    """

    # Return true if all Queens are placed
    if row == grid.bounds:
        return True

    curr_queen = Queen(row)
    curr_queen.get_possibles(grid)

    while curr_queen.possibles:
        curr_queen.col = curr_queen.possibles.popleft()

        new_grid = Grid(grid.bounds, deepcopy(grid.layout))
        new_grid.update_squares(curr_queen)
        success = do_place_queen(new_grid, row+1, queens)
        if success:
            queens[row] = curr_queen
            return True

    return False


def place_all_queens(n):
    """ Place all queens on the grid. """

    success = False

    if type(n) == int and n >= 4:

        queens = [0] * n
        grid = Grid(n)
        row = 0

        success = do_place_queen(grid, row, queens)

    return queens if success else "Not Possible"
