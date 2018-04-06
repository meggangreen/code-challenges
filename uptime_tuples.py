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

def get_total_uptime(network_t):
    """ Returns one list of tuples representing overall network uptime. """

    total_uptime = []
    end_time = network_t[0][-1][0]

    ideal_uptime = [(end_time, 1)]  # Ideal is up (1) for entire time

    for device_t in network_t:
        # Exit this device, and possibly this function, early
        if len(device_t) == 1:
            if device_t == [(end_time, 0)]:  # Device was down 100%
                return device_t
            else:
                continue  # Device was up 100%; skip it
        start_time = 0
        for t in device_t:


    return total_uptime
