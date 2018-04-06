# Given by Adam Berman of Cisco Meraki; adam.berman@meraki.net

# A given list of tuples that represent the time marker in milliseconds at state
# change and a state marker of 1 (up) or 0 (down) for one device. Given a list
# of the time-state tuples for many -- thousands -- of devices, and operating on
# the axiom that if one device is down, the entire network is down, represent
# the overall network time and state in one list of tuples.
#
# Eg: [[(2000, 1), (3000, 0), (6000, 1)], ==> [(2000, 1), (4000, 0), (6000, 1)]
#      [(3000, 1), (4000, 0), (6000, 1)],
#      [(6000, 1)]]
#
# Optimized answer uses in O(nlogn) time and space.
#


