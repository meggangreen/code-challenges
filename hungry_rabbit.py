def find_center(garden):
    """ Return the rabbit's starting point as a coordinate (j, i), as in garden[j][i]. """

    # Find center: j is 'row', i is 'col'
    # Initialize j and i, rows and cols
    j, i = -1, -1
    num_rows = len(garden)
    num_cols = len(garden[0])

    # This section should be cleaned up before pushing
    if num_rows % 2 != 0:
        j = num_rows // 2
    else:
        j1, j2 = num_rows // 2, num_rows // 2 - 1

    if j != -1:
        if num_cols % 2 != 0:
            i = num_cols // 2
        else:
            # Find the most carrots near the center of the row j
            i = garden[j].index(max(garden[j][num_cols//2], garden[j][num_cols//2]-1))

    else:
        if num_cols % 2 != 0:
            i1 = garden[j1][num_cols//2]
            i2 = garden[j2][num_cols//2]
        else:
            i1 = max(garden[j1][num_cols//2], garden[j1][num_cols//2]-1)
            i2 = max(garden[j2][num_cols//2], garden[j2][num_cols//2]-1)

        ival = max(i1, i2)
        if ival == i1:
            j = j1
        else:
            j = j2

        i = garden[j].index(ival)

    return (j, i)


def eat_carrots(garden, start):
    """ Return number of carrots eaten where garden is the matrix and start is
        (j, i) as in garden[j][i].

    """

    # start[0] is row, [1] is col
    # Get first snack amount
    carrots = garden[start[0]][start[1]]
    # Guard against infinite loops
    garden[start[0]][start[1]] = 0

    pos = start
    while True:
        pos = choose_next(garden, pos)
        if not pos:  # Found no more adjacent carrots
            return carrots
        carrots += garden[pos[0]][pos[1]]
        garden[pos[0]][pos[1]] = 0


def choose_next(garden, pos):
    """ Get next position as (j, i) coordinate based on largest value.

        This is kind of similar to finding the first position and there
        may be a way to refactor and combine.

    """

    north = garden[pos[0] - 1][pos[1]] if pos[0] != 0 else -1
    south = garden[pos[0] + 1][pos[1]] if pos[0] != len(garden)-1 else -1
    east = garden[pos[0]][pos[1]+1] if pos[1] != len(garden[pos[0]])-1 else -1
    west = garden[pos[0]][pos[1]-1] if pos[1] != 0 else -1

    # I'm sure there is a shorter way for these as well
    max_val = max(north, south, east, west)
    next_pos = None
    if max_val == 0:  # No more adjacent carrots
        next_pos == None
    elif max_val == north:
        next_pos = (pos[0] - 1, pos[1])
    elif max_val == south:
        next_pos = (pos[0] + 1, pos[1])
    elif max_val == east:
        next_pos = (pos[0], pos[1] + 1)
    elif max_val == west:
        next_pos = (pos[0], pos[1] - 1)

    return next_pos


if __name__ == '__main__':
    garden = [[5, 3, 0, 7, 1],
              [2, 4, 7, 3, 9],
              [9, 7, 1, 3, 5],
              [4, 0, 1, 6, 5],
              [8, 2, 6, 9, 8]]

    start = find_center(garden)

    carrots = eat_carrots(garden, start)

    print(carrots)  # expect 104
