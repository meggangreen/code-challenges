# Given by Adam Berman of Cisco Meraki; adam.berman@meraki.net

# A given list of tuples that represent the time marker in milliseconds at state
# change and a state marker of 1 (up) or 0 (down) for one device. Given a list
# of the time-state tuples for many -- thousands -- of devices, and operating on
# the axiom that if one device is down, the entire network is down, represent
# the overall network time and state in one list of tuples.
#
# Eg: [[(2000, 1), (3000, 0), (6000, 1)], ==> [(2000, 1), (4000, 0), (6000, 1)]
#      [(3000, 1), (4000, 0), (5000, 1), (6000, 0)],
#      [(6000, 1)]]
#
# Optimized answer uses in O(nlogn) time and space.
#

def get_total_uptime(network_uptime):
    """ Returns one list of tuples representing overall network uptime. """

    total_uptime = []
    end_time = network_uptime[0][-1][0]  # Final timestamp

    ideal_uptime = (end_time, 1)  # Ideal is up (1) for entire time

    for device_uptime in network_uptime:
        # Exit this device, and possibly this function, early
        if network_uptime.index(device_uptime) == 0:
            total_uptime = network_uptime[0]
            continue
        if len(device_uptime) == 1:
            if device_uptime != [ideal_uptime]:  # Device was down 100%
                return device_uptime
            else:
                continue  # Device was up 100%; skip it
        total_uptime = combine_uptimes(device_uptime, total_uptime)

    return total_uptime


def combine_uptimes(device, total):
    """ Combines or flattens two lists of time-state tuples. """

    # when states match:
    # if state == 1, take min time
    # if state == 0, take max time
    # increase both i

    # when states don't match:
    # take 0 state tuple
    # increase 0 state tuple i
    # no change to other i
    # (states should now match for the rest of lists)

    d, t = 0, 0

    combined = []
    while d < len(device) or t < len(total):
        # Break out when index markers reach len(list)
        if d = len(device):
            combined.extend([total[t] for t in range(t, len(total))])
            break
        if t = len(total):
            combined.extend([device[d] for d in range(d, len(device))])
            break

        # Initialize or reset variables
        time, state = None, None

        # If states -- list[i][1] -- match:
        if device[d][1] == total[t][1]:
            state = total[t][1]

            # Take min uptime or max downtime
            if state == 1:
                time = min(device[d][0], total[t][0])
            else:
                time = max(device[d][0], total[t][0])

            # Increment both index markers
            d += 1
            t += 1

        # Otherwise, take the downtime tuple and increase its list index marker
        elif device[d][1] == 0:
            time, state, d  = device[d][0], device[d][1], d + 1
        elif total[t][1] == 0:
            time, state, t  = total[t][0], total[t][1], t + 1
        # The states should match for the rest of the lists

        # Append time-state tuple to combined
        combined.append((time, state))

    return combined


