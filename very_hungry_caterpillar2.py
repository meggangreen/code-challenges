def get_uneaten_leaves(branch_length, caterpillars):
    """ Returns number of uneaten leaves after all caterpillars have eaten. """

    if type(branch_length) != int:
        return None

    if branch_length < 1:
        return 0

    if 1 in caterpillars:
        return 0

    # Validate and pare-down caterpillars
    actual_cats = get_prime_caterpillars(validate_caterpillars(caterpillars))

    if not actual_cats:
        return branch_length

    leaves = branch_length

    # Subtract the leaves for each caterpillar
    for caterpillar in actual_cats:
        leaves -= branch_length // caterpillar

    # Add back in leaves that have been double-counted
    for i in range(len(actual_cats)):
        for j in range(i+1, len(actual_cats)):
            leaves += branch_length // (actual_cats[i] * actual_cats[j])

    return leaves


def get_prime_caterpillars(caterpillars):
    """ Removes caterpillars whose hop interval is a multiple of another's. """

    prime_cats = caterpillars[:]

    for j in range(len(prime_cats)-1, -1, -1):
        for i in range(j):
            if prime_cats[j] % prime_cats[i] == 0:
                prime_cats[j] = -1

    return list(filter(lambda x: x > 0, prime_cats))


def validate_caterpillars(caterpillars):
    """ Validates each caterpillar. """

    valid_cats = caterpillars[:]

    for j in range(len(valid_cats)):
        if not valid_cats[j] or type(valid_cats[j]) != int or valid_cats[j] < 1:
            valid_cats[j] = -1

    return list(filter(lambda x: x > 0, valid_cats))
