""" Find the nth root of k. """

# If anyone is interested in my thoughts on why this is asinine for a junior
# software engineer, I'm happy to share.
# Given y = x**n, find x from y & n ... without using the very simple x = y**(1/n)
# IE: write the min-max-avg method a calculator would use to solve a root

def calc_root_shifting_point(radicand, index):

    if radicand < 0 or index < 1:
        return None

    if index == 1:
        return radicand

    # Set up blocks of numbers (move to helper func)
    rad_s = str(radicand)
    dec = rad_s.find('.')
    rad_s = rad_s[:dec] + rad_s[dec+1:]
    rem = len(rad_s) % index if len(rad_s) % index != 0 else index
    blocks = ['0' * index] * len(rad_s) // index + 1
    blocks[0] = [:rem]
    blocks[1:] = [rad_s[j:j+index] for j in range(rem, len(rad_s), index)]


