

def all_palindromes(s):
    """ Returns a list of distinct contiguous sub-strings of 1+ characters.

        >>> all_palindromes('abbabbaac')
        ['a', 'aa', 'abba', 'abbabba', 'b', 'bab', 'bb', 'bbabb', 'c']

    """

    pals = set([])

    for i in range(len(s)):
        pals.add(s[i])  # add each char

        # Odd-numbered palindromes
        for j in range(len(s)):
            if i - j < 0 or i + j >= len(s) or s[i-j] != s[i+j]:
                break
            pals.add(s[i-j:i+j+1])

        # Even-numbered palindromes
        for j in range(len(s)):
            if i - j < 0 or i + 1 + j >= len(s) or s[i-j] != s[i+1+j]:
                break
            pals.add(s[i-j:i+1+j+1])

    return sorted(list(pals))
