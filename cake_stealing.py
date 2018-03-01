""" Cake stealing, or metal rod cutting, or knapsac carrying problem.
    Solution from InterviewCake, with modifications for my preference and
    understanding.

"""

def max_cake_payoff(cakes, capacity):
    """
        >>> cakes = [ (3, 34), (7, 52), (4, 14), (6, 28) ]
        >>> capacity = 25
        >>> max_cake_payoff(cakes, capacity)


    """

    # We make a list to hold the maximum possible value at every bag weight
    # capacity from 0 to 'capacity' starting each index with value 0
    max_payoffs_at_capacities = [0] * (capacity + 1)

    for curr_capacity in xrange(capacity + 1):
        # Set a variable to hold the running max payoff for curr_capacity
        curr_max_payoff = 0

        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value, we can steal cakes
            # to infinity and beyond
            if cake_weight == 0 and cake_value > 0:
                return float('inf')

            # If the current cake weighs as much or less than the curr_capacity,
            # it's possible taking the cake would get a better value
            if cake_weight <= curr_capacity:

                # So we check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_payoffs_at_capacities
                max_payoff_using_cake = (
                    cake_value
                    + max_payoffs_at_capacities[curr_capacity - cake_weight]
                )

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the curr_max_payoff?
                curr_max_payoff = max(max_payoff_using_cake,
                                        curr_max_payoff)

        # Add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_payoffs_at_capacities[curr_capacity] = curr_max_payoff

    return max_payoffs_at_capacities[capacity]