""" Caterpillars Eating Leaves """

class Leaf(object):
    """ A node that has a value and knows its next node. """

    def __init__(self, val):
        self.val = val
        self.next = None


class Branch(object):
    """ A linked list that has a root node and knows its length. """

    def __init__(self, root_val=1, length=1):
        self.root = Leaf(root_val)
        self.length = length


    def make_leaves(self):
        """ Make all the leaves in the branch. """

        curr_leaf = self.root
        i = 1
        while i < self.length:
            next_leaf = Leaf(curr_leaf.val+1)
            curr_leaf.next = next_leaf
            curr_leaf = next_leaf
            i += 1


    def get_leaves(self):
        """ Returns a list of leaves whose value is not -1 (eaten). """

        leaves = []
        curr_leaf = self.root
        while curr_leaf:
            if curr_leaf.val != -1:
                leaves.append(curr_leaf.val)
            curr_leaf = curr_leaf.next

        return leaves


class Caterpillar(object):
    """ A bug that eating every kth (hop interval) leaf in a branch. """

    def __init__(self, hop_interval=0):
        """ Hop interval of 0 means this caterpillar does not eat. """

        self.hop_interval = hop_interval


    def eat_leaves(self, branch):
        """ Given a branch, eat every leaf at self.hop_interval. """

        if self.hop_interval < 1:
            return

        curr_leaf = branch.root
        while curr_leaf:
            if curr_leaf.val % self.hop_interval == 0:
                curr_leaf.val = -1
            curr_leaf = curr_leaf.next


def get_remaining_leaves_from_branch(branch_length, caterpillars):
    """ Returns the number of intact leaves after all the caterpillars have eaten. """

    branch = Branch(length=branch_length)
    branch.make_leaves()

    for hop_interval in caterpillars:
        caterpillar = Caterpillar(hop_interval)
        caterpillar.eat_leaves(branch)

    leaves = branch.get_leaves()

    return len(leaves)


def get_prime_caterpillars(caterpillars):
    """ Removes caterpillars whose hop interval is a multiple of another's. """

    prime_cats = caterpillars

    for j in range(len(prime_cats)-1, -1, -1):
        for i in range(j):
            if prime_cats[j] % prime_cats[i] == 0:
                prime_cats[j] = -1

    return list(filter(lambda x: x > 0, prime_cats))


def get_uneaten_leaves(branch_length, caterpillars):
    """ Breaks up branches and/or caterpillars as necessary to get the total
        uneaten leave, regardless of the massive branch size or giant quantity
        of hungry caterpillars snacking on it.

    """

    if type(branch_length) != int:
        return None

    if branch_length <= 0:
        return 0

    if not caterpillars:
        return branch_length

    # Break up caterpillars
    prime_cats = get_prime_caterpillars(caterpillars)

    branch_break = prime_cats[-1]  # Requires list is sorted
    multi = branch_length // branch_break
    remainder = branch_length % branch_break
    # Get "whole-branch" leaves
    leaf_c = get_remaining_leaves_from_branch(branch_break, prime_cats) * multi
    # Get partial-branch leaves, if any
    if remainder:
        leaf_c += get_remaining_leaves_from_branch(remainder, prime_cats)

    return leaf_c
