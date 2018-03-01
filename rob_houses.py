""" Classic house-robbing problem -- interesting piece is holding on to a whole
    array of values as opposed to just current_max and next_house, for example.

"""

street = [3, 50, 34, 0, 863, 25]
avenue = [45, 72, 86, 20, 58, 10, 33]
circle = [1, 5, 9, 7, 3, 2, 8, 6, 4]

def rob_max_value(houses):
    """ Return the maximum possible value of robbing houses. The robbed houses
        cannot be adjacent.

        >>> rob_max_value(street)


        >>> rob_max_value(avenue)


        >>> rob_max_value(circle)


    """

    values = []

    if len(houses) == 0:
        return 0

    if len(houses) == 1:
        return houses[0]

    values.append(max(houses[0], houses[1]))

    for i in range(2, len(houses)):
        values.append(max(values[i-1], values[i-2] + houses[i]))

    return values[-1]


#############################
if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\n----- ALL TESTS PASSED -----\n")