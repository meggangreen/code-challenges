""" Word Break -- a common CS problem

    Given a string 'string' and an array of words 'words', determine if the
    string can be broken up into a space-separated sequence of one or more words.

"""

def is_word_sequence(string, words):
    """ Returns True/False.

        >>> string = 'applebananacherry'
        >>> words = ['apple', 'banana', 'cherry', 'durian']
        >>> is_word_sequence(string, words)
        True

        >>> string = 'applebanacherry'
        >>> is_word_sequence(string, words)
        False

    """

    # Start tracking array with 0th element for for-loop logic
    tested = [True]

    for i in xrange(len(string)):  # for memory's sake, don't generate new list
        tested.append(False)
        for j in xrange(i, -1, -1):  # build from right to left
            if (tested[j] is True) and (string[j:i+1] in words):
                tested[i+1] = True
                break

    return tested[-1]


#############################

if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\n----- ALL TESTS PASSED -----\n")