""" Firnd the middle permutation in a sorted list of all permutations

You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering
these strings in dictionary order, return the middle term. (If the sequence has
an even length n, define its middle term to be the (n/2)th term.)

Example
For s = "abc", the result should be "bac".

The permutations in order are:
["abc", "acb", "bac", "bca", "cab", "cba"]
So, The middle term is "bac".:
["abc", "acb", "bac", "bca", "cab", "cba"]

"""

def find_all_permutations(s):
    """ Returns a list of all possible permutations.

        >>> find_all_permutations('bac')
        ['bac', 'bca', 'abc', 'acb', 'cba', 'cab']

    """

    if len(s) == 0:
        return []

    if len(s) == 1:
        return s

    permutations = []

    for i in range(len(s)):
        current = s[i]
        remaining = s[:i] + s[i+1:]

        for permutation in find_all_permutations(remaining):
            permutations.append(current + permutation)

    return permutations


def find_middle_permutation(s):
    """ Returns the string located at the midpoint of the sorted list.

        >>> find_middle_permutation('bac')
        'bac'

    """
    from math import ceil


    if len(s) == 0:
        return None

    if len(s) == 1:
        return s

    permutations = find_all_permutations(s)

    return sorted(permutations)[int(ceil(len(permutations))/2.0)-1]
