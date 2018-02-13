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
# management_pairs = [
#     ('Ben', 'Charlie'),
#     ('Alice', 'Ben'),
#     ('Ben', 'Denis'),
# ]
#
# == Output
#
# > create_mangement_tree(management_pairs)
#
# >> Node(
#       name='Alice',
#       reportees=[
#           Node(name='Ben' ....),
#       ],
#    )

