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
                 ('Alice', 'Fiona'),
                 ('Fiona', 'Eva'),
                 ]
#
# == Output
#
# >>> create_mangement_tree(management_pairs)
#
#   Node(name='Alice', reportees=[
#       Node(name='Benji', reportees=[
#           Node(name='Cherise', reportees=[]),
#           Node(name='Denise', reportees=[])
#           ]),
#       Node(name='Fiona', reportees=[
#           Node(name='Eva', reportees=[]),
#           ]),
#       ])

class Employee(object):

    def __init__(self, name, reportees=[]):
        self.name = name                    # Name as string;
        self.reportees = reportees          # Reportees as list of Employees

    def __repr__(self):
        return "<Employee {}>".format(self.name)

    def add_reportee(self, reportee):  # reportee as Employee
        self.reportees.append(reportee)


def create_management_tree(mgr_rpt_pairs):

    inorder(get_management_root(create_employees(mgr_rpt_pairs)))


def inorder(employee, level=0):
    """ Given root, prints employee tree. Recurses, printing on the way down. """

    if employee:
        level += 1
        print employee.name
        for reportee in employee.reportees:
            print "    " * level,
            inorder(reportee, level)


def create_employees(mgr_rpt_pairs):
    """ Create dict of Employee objects. """

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
    """ Return root - employee who is not a reportee - for tree assembly. """

    reportees_set = set()
    employees_set = set(employees.values())
    for emp in employees_set:
        reportees_set |= set(emp.reportees)

    root = (employees_set - reportees_set).pop()

    return root


########################################
if __name__ == '__main__':
    create_management_tree(mgr_rpt_pairs)
