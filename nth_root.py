""" Find the nth root of k. """

# If anyone is interested in my thoughts on why this is asinine for a junior
# software engineer, I'm happy to share.
# Given y = x**n, find x from y & n ... without using the very simple x = y**(1/n)
# IE: write the min-max-avg method a calculator would use to solve a root

def calc_root(radicand, index):

    if radicand < 1 or index < 0:
        return None

    if index == 1:
        return radicand

    radicand_s = str(radicand)
    blocks[1] = radicand_s[]
    blocks = [num[i:i+index:index]]
