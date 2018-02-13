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

class Employee(object):

    def __init__(self, name, reportees=[]):  # name as string; reportees as list
        self.name = name
        self.reportees = reportees

    def __repr__(self):
        return "<Employee {}>".format(self.name)

    def add_reportee(self, reportee):  # reportee as Employee
        self.reportees.append(reportee)


def inorder(employee, level=0):
    if employee:
        level += 1
        print employee.name
        for reportee in employee.reportees:
            print "    " * level,
            inorder(reportee, level)


def create_employees(mgr_rpt_pairs):

    # create dict of employee nodes
    employees = {}

    for mgr, rpt in mgr_rpt_pairs:
        if not rpt in employees:
            employees[rpt] = Employee(rpt, [])
        if not mgr in employees:
            employees[mgr] = Employee(mgr, [employees[rpt]])
        else:
            employees[mgr].add_reportee(employees[rpt])

    return employees


def get_management_root(employees):
    """ return root for tree assembly """

    reportees_set = set()
    employees_set = set(employees.values())
    for emp in employees_set:
        reportees_set |= emp.reportees

    root = (employees_set - reportees_set).pop()

    return root


class Tree(object):

    def __init__(self, root):  # root as Employee
        self.root = root

    def __repr__(self):
        return "<Tree with root {}".format(self.root)

    def build_tree(self, employees):  # employees as dictionary
        pass


def create_management_tree(mgr_rpt_pairs):  # root as str; employees as dict

    # get employees and root
    employees = create_employees(mgr_rpt_pairs)
    root = get_management_root(employees)


    # breadth-first traversal of dictionary to make tree
    # start with root's reportees
    emp_queue = deque()
    emp_queue.append(root)

    while emp_queue:
        # get current manager (first pass will be root!)
        curr_mgr = emp_queue.popleft()

        # add reportees to emp queue
        emp_queue.extend(employees[curr_mgr])

        # make node for current manager
        curr_mgr_node = Employee(curr_mgr)

        # start tree if necessary
        if not tree:
            tree = Tree(curr_mgr_node)

        if prev_mgr_node:
            prev_mgr_node.add_reportee(curr_mgr_node)
