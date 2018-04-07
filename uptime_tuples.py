# Given by Adam Berman of Cisco Meraki; adam.berman@meraki.net

# A given list of tuples represents the time marker in milliseconds at state
# change and a state marker of 1 (up) or 0 (down) for one device. Given a list
# of the time-state tuples for many -- thousands -- of devices, and operating on
# the axiom that if one device is down, the entire network is down, represent
# the overall network time and state in one list of tuples.
#
# Eg: [[(2000, 1), (3000, 0), (6000, 1)], ==> [(2000, 1), (4000, 0), (5000, 1), (6000, 0)]
#      [(3000, 1), (4000, 0), (5000, 1), (6000, 0)],
#      [(6000, 1)]]
#
# Optimized answer uses in O(nlogn) time and space.
#


# This started to look like merge sort, which makes me think we can do the
# combination func recursively on a pair of devices and build up like a NCAA
# bracket to a final combination -- is that how we get to O(nlogn) time?


def get_total_uptime(network_uptimes):
    """ Returns one list of tuples representing overall network uptime.

        >>> uptimes = [[(2000, 1), (3000, 0), (6000, 1)],
                       [(3000, 1), (4000, 0), (5000, 1), (6000, 0)],
                       [(6000, 1)]]
        >>> get_total_uptime(uptimes)
        [(2000, 1), (4000, 0), (5000, 1), (6000, 0)]

    """

    total_uptime = []
    end_time = network_uptimes[0][-1][0]  # Final timestamp

    for device_uptime in network_uptimes:

        # Ways to exit this device, and possibly this function, early:
        # if device_uptime == [(end_time, 0)]:  # Device was down 100%; return
        #     return device_uptime

        if not total_uptime:  # At first run
            total_uptime = device_uptime
            continue

        # if device_uptime == [(end_time, 1)]:  # Device was up 100%; skip combine
        #     continue

        # if device_uptime == total_uptime:  # Combining would be redundant
        #     continue

        # If we're still going, then merge lists
        total_uptime = combine_uptimes([device_uptime, total_uptime])

    return total_uptime


def combine_uptimes(uptimes):
    """ Combines two lists of time-state tuples. Runs recursively if called on
        more than two devices.

        >>> uptimes = [[(2000, 1), (3000, 0), (6000, 1)],
                       [(3000, 1), (4000, 0), (5000, 1), (6000, 0)],
                       [(6000, 1)]]
        >>> get_total_uptime(uptimes)
        [(2000, 1), (4000, 0), (5000, 1), (6000, 0)]

    """

    # when states match:
    # if state == 1, take min time
    # if state == 0, take max time
    # increase both i

    # when states don't match:
    # take 0 state tuple
    # increase 0 state tuple i
    # no change to other i
    # (states should now match for the rest of lists)

    print(uptimes)
    import pdb; pdb.set_trace()

    if len(uptimes) == 1:
        return uptimes[0]
    elif len(uptimes) > 2:
        i = len(uptimes) // 2
        a_uptimes = combine_uptimes(uptimes[:i])
        b_uptimes = combine_uptimes(uptimes[i:])
    else:
        a_uptimes = uptimes[0]
        b_uptimes = uptimes[1]

    # Set final time; should be same always; used for best/worst scenario
    end_time = uptimes[0][-1][0]

    # Ways to exit early:
    # Best or Worst possible uptime
    if a_uptimes == [(end_time, 0)] or b_uptimes == [(end_time, 1)]:
        return a_uptimes
    if b_uptimes == [(end_time, 0)] or a_uptimes == [(end_time, 1)]:
        return b_uptimes
    # Uptimes are equal
    if a_uptimes == b_uptimes:
        return a_uptimes

    # Let's start
    a, b = 0, 0
    combined = []

    while a < len(a_uptimes) or b < len(b_uptimes):
        # Break out when index markers reach len(list)
        if a == len(a_uptimes):
            combined.extend([b_uptimes[b] for b in range(b, len(b_uptimes))])
            break
        if b == len(b_uptimes):
            combined.extend([a_uptimes[a] for a in range(a, len(a_uptimes))])
            break

        # Initialize or reset variables
        time, state = None, None

        # If states -- list[i][1] -- match:
        if a_uptimes[a][1] == b_uptimes[b][1]:
            state = b_uptimes[b][1]

            # Take min uptime or max downtime
            if state == 1:
                time = min(a_uptimes[a][0], b_uptimes[b][0])
            else:
                time = max(a_uptimes[a][0], b_uptimes[b][0])

            # Increment both index markers
            a += 1
            b += 1

        # Otherwise, take the downtime tuple and increase its list index marker
        elif a_uptimes[a][1] == 0:
            time, state, a = a_uptimes[a][0], a_uptimes[a][1], a + 1
        elif b_uptimes[b][1] == 0:
            time, state, b = b_uptimes[b][0], b_uptimes[b][1], t + 1
        # The states should match for the rest of the lists

        # Append time-state tuple to combined
        combined.append((time, state))

    return combined
