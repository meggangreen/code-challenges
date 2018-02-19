def is_subset(set1, set2):
    """ A substitution for issubset().

        >>> set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
        >>> set2 = set([])
        >>> is_subset(set1, set2)
        False

        >>> set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
        >>> set2 = set([1, 3, 9])
        >>> is_subset(set1, set2)
        False

        >>> set1 = set([1, 2, 3, 4, 5, 6, 7, 8])
        >>> set2 = set([1, 3, 5, 7])
        >>> is_subset(set1, set2)
        True

    """

    if not set1 or not set2:
        return False

    return len(set1 & set2) == min(len(set1), len(set2))


#############################

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\n----- ALL TESTS PASSED -----\n")
