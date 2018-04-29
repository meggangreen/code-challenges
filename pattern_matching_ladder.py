""" Pattern Matching with Ladder """

"""

#
# Function 1. is_match (difficulty 1)
#

Lets implement a function called `is_match`.

`is_match(pattern, input)`
"pattern" is a string where each character is a token.
"input" is a string where each word is a token (space delimited).
return value: boolean which represents whether these two strings match

Here are some python examples / test cases:
assert is_match("aba", "red blue red") == True
assert is_match("aaa", "red blue red") == False
assert is_match("aba", "red red red") == False

Implement `is_match` with linear runtime O(n + m) where n is the length of
pattern and m is the length of input. You can use any language you want. If you
finish with enough time left then see if you can make your implementation as
clean and concise as possible.

"""

def is_match(pattern, input_s):
    """ Returns True/False

        >>> is_match("aba", "red blue red")
        True

        >>> is_match("aaa", "red blue red")
        False

        >>> is_match("aba", "red red red")
        False

        >>> is_match('abc', 'red blue red')
        False

    """

    input_lst = input_s.strip().split()
    if len(input_lst) != len(pattern):
        return False

    pat_str = {}

    # this breaks down if any word in input_s is also a token:
    # is_match('abc', 'bowl a chicken') is False but should be True
    for i in range(len(pattern)):
        if pattern[i] in pat_str:
            if input_lst[i] != pat_str[pattern[i]]:
                return False
        elif input_lst[i] in pat_str:
            if pattern[i] != pat_str[input_lst[i]]:
                return False
        else:  # First time of token and word
            pat_str[input_lst[i]] = pattern[i]
            pat_str[pattern[i]] = input_lst[i]

    # If we've made it without incident, must be True
    return True


"""

#
# Function 2. find_combos (difficulty 2)
#

Lets implement a function called `find_combos`.

`find_combos(num_desired, available_pack_sizes)`
"num_desired" is an integer and represents the number of sodas that you want.
"available_pack_sizes" is a list of integers and reprents the available pack
sizes a store has.
return value: a list of lists where each entry is a valid combination

If you ran find_combos at the python REPL you'd want to see exactly this output:
>>> find_combos(7, [1, 6, 12])
[[1, 1, 1, 1, 1, 1, 1,], [1, 6]]
>>> find_combos(7, [6])
[]
>>> find_combos(4, [1, 3])
[[1, 1, 1, 1], [1, 3]]

Implement `find_combos` in the simplest way you can. There are no points for
efficiency or runtime in this question. Just focus on solving it in the
cleanest way possible.  You can use any language you want. If you finish
everything else with enough time left then see if you can write some type of
upper bound on the runtime (asymptotic runtime complexity).

"""

def find_combos(num_desired, available_pack_sizes):

    # Started by thinking this was a Making Change problem; I am now convinced
    # it is the Rod-Cutting problem. I first saw the problem in another
    # technical screen. As a person who is not a CS graduate, I have not spent
    # time really studying this problem. It is complex and interesting-ish, but
    # not part of my wheel-house of strengths.

    pass


"""

#
# Function 3. is_match_2 (difficulty 3)
#
# This is a BONUS QUESTION. I don't expect you'll be able to get to this
# question and solve it in time.
#

Lets implement a function called `is_match_2`.

`is_match(pattern, input)`
"pattern" is a string where each character is a token.
"input" is a string.
return value: boolean which represents whether there exists any solution.

Here are some python examples / test cases:
assert is_match("ab", "xy") == True
assert is_match("ab", "xxy") == True
assert is_match("ab", "xyy") == True
assert is_match("ab", "xx") == False
assert is_match("aa", "xy") == False

Implement `is_match_2` in the simplest way possible. You can use any language
you want. If you finish with enough time left then see if you can make your
implementation as clean and concise as possible.

"""

def is_match_2(pattern, input_s):
    """ Return True/False if the pattern exists anywhere in the input string,
        this time evaluating characters instead of words.

        This method takes advantage of the ord() function to calculate the
        difference between the each character and its right-side neighbor in the
        pattern and match it to the differences in the input_s characters.

        >>> is_match_2("ab", "xy")
        True

        >>> is_match_2("ab", "xxy")
        True

        >>> is_match_2("ab", "xyy")
        True

        >>> is_match_2("ab", "xx")
        False

        >>> is_match_2("aa", "xy")
        False

    """

    # Walk through input_s; start pattern comparison at each new i
    # Subtract number of changes to avoid index errors in matching
    for i in range(len(input_s) - (len(pattern)-1)):

        # Start with an unsuccessful array
        successes = [0] * (len(pattern)-1)

        # Walk through pattern
        for j in range(len(pattern)-1):

            # Get the difference between ordinals to compare
            actual = ord(input_s[i+j]) - ord(input_s[i+j+1])
            # If the pattern is going to be long and repeated, we could memoize
            # the differences to reduce calculations; but I'm not sure if a
            # lookup has the same cost as a simple low-integer subtraction
            required = ord(pattern[j]) - ord(pattern[j+1])

            if actual == required:
                # Mark a success for each match
                successes[j] = 1
            else:
                del successes
                break  # Go to next i
            if sum(successes) == len(pattern) - 1:
                # Return as soon as a matching substring is found
                return True

    return False


################################################################################

if __name__ == '__main__':
    import doctest
    doctest.testmod()
