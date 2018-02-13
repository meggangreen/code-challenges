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
# management_pairs = [('Ben', 'Charlie'),
#                     ('Alice', 'Ben'),
#                     ('Ben', 'Denis'),
#                     ]
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

class Node(object):

    def __init__(self, name=None):
        self.name = name
        self.reportees = []

    def __repr__(self):
        return "<Node {}>".format(self.name)

    def add_reportee(self, reportee=None):
        if reportee:
            self.reportees.append(reportee)


def create_management_tree(mgr_emp_pairs):
    nodes = {}

    for mgr, emp in mgr_emp_pairs:
        if not mgr in nodes:
            new_node = Node(mgr)
            new_node.add_reportee(emp)
            nodes[mgr] = new_node
        else:
            nodes[mgr].add_reportee(emp)


