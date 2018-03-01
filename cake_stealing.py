""" Cake stealing, or metal rod cutting, or knapsac carrying problem.
    Solution from InterviewCake, with modifications for my preference and
    understanding.

"""

def max_duffel_bag_value(cakes, capacity):
    """
        >>> cakes = [ (3, 34), (7, 52), (4, 14), (6, 28) ]
        >>> capacity = 25


    """

    # We make a list to hold the maximum possible value at every bag weight
    # capacity from 0 to 'capacity' starting each index with value 0
    max_values_at_capacities = [0] * (capacity + 1)

    for current_capacity in xrange(capacity + 1):
        # Set a variable to hold the max monetary value so far
        # for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value the value of
            # our duffel bag is infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # If the current cake weighs as much or less than the
            # current weight capacity it's possible taking the cake
            # would get a better value
            if cake_weight <= current_capacity:

                # So we check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_values_at_capacities
                max_value_using_cake = (
                    cake_value
                    + max_values_at_capacities[current_capacity - cake_weight]
                )

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake,
                                        current_max_value)

        # Add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[capacity]