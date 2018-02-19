# Problem from codewars.com

def alphabet_position(text):
    """ What amsowie and I wrote.

        >>> text = "The sunset sets at twelve o' clock."
        >>> alphabet_position(text)
        "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

    """

    alpha_pos_lookup = {chr(i + 96): i for i in range(1, 27)}

    text = text.lower()
    t_list = []

    for t in text:
        if t in alpha_pos_lookup:
            t_list.append(str(alpha_pos_lookup[t]))

    return ' '.join(t_list)


def alphabet_position_oneline(text):
    """ Voted best solution on codewars.com.

        >>> text = "The sunset sets at twelve o' clock."
        >>> alphabet_position_oneline(text)
        "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

    """

    return ' '.join(str(ord(t) - 96) for t in text.lower() if t.isalpha())


#############################

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\n----- ALL TESTS PASSED -----\n")
