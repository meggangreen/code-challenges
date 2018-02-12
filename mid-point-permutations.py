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

    """

    if len(s) == 0:
        return []

    if len(s) == 1:
        return s

    permutations = []

    for i in range(len(s)):
        current = s[i]
        remaining = s[:i] + s[i+1:]

        for p in find_all_permutations(remaining):
            permutations.append(current + p)

    return permutations


def find_middle_permutation(permutations):
    """ Returns the string located at the midpoint of the sorted list.

    """
    from math import ceil

    if len(permutations) == 0:
        return None

    if len(permutations) == 1:
        return permutations[0]

    return permutations[ceil(len(sorted(permutations))/2.0)]
