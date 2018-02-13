# Suppose we have a file with manager and reportee pairs (manager, reportee)
# and we would like to convert this into a tree structure.
#
# Write a function create_mangement_tree which given a list of
# (manager, reportee) pairs creates a tree and returns the root.
#
# Tree Node Data Structure:
#
#     class Node(object):
#         name = ''          # Name of the employee
#         reportees = []     # Reportees list of type Node
#
# ===== Example
#
#        Alice
#          |
#         Ben
#       /     \
#   Charlie   Denis
#
# == Input
# #
mgr_rpt_pairs = [('Benji', 'Cherise'),
                 ('Alice', 'Benji'),
                 ('Benji', 'Denise'),
                 ]
#
# == Output
#
# >>> create_mangement_tree(management_pairs)
#
#   Node(name='Alice', reportees=[
#       Node(name='Ben', reportees=[
#           Node(name='Charlie', reportees=[]),
#           Node(name='Denis', reportees=[])
#           ]),
#       ])

from collections import deque

class Node(object):

    def __init__(self, name):  # name as string
        self.name = name
        self.reportees = []

    def __repr__(self):
        return "<Node {}>".format(self.name)

    def add_reportee(self, reportee):  # reportee as string or Node
        if type(reportee) == str:
            reportee = Node(reportee)
        self.reportees.append(reportee)


class Tree(object):

    def __init__(self, root):  # root as Node
        self.root = root

    def __repr__(self):
        return "<Tree with root {}".format(self.root)

    def build_tree(self, employees):  # employees as dictionary
        pass


def create_management_tree(mgr_rpt_pairs):  # root as str; employees as dict

    # get employees and root
    employees = create_employees(mgr_rpt_pairs)
    root = get_management_root(employees)

    # start tree
    root_node = Node(root)
    tree = Tree(root_node)

    # breadth-first traversal of dictionary to make tree
    emp_queue = deque()

    for rpt in employees[root]:
        root_node.add_reportee(rpt)



def create_employees(mgr_rpt_pairs):

    # create dict of mgr nodes with list of names only in node.reportees
    employees = {}
    for mgr, rpt in mgr_rpt_pairs:
        if not mgr in employees:
            employees[mgr] = []
        employees[mgr].append(rpt)

    return employees


def get_management_root(employees):
    """ return root for tree assembly """

    # get set of all reportees (sometimes people have more than 1 boss)
    reportees_set = set()
    for rpt in employees.itervalues():
        reportees_set.add(rpt)

    managers_set = employees.viewkeys()

    root = (managers_set - reportees_set).pop()

    return root

