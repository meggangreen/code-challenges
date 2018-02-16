def is_subset(set1, set2):
    """ A substitution for issubset(). """

    if not set1 or not set2:
        return False

    return len(set1 & set2) == min(len(set1), len(set2))