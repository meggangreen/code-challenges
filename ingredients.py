
def get_dishes_by_ingredient(dishes):
    """ Returns a matrix of ingredients of which two or more dishes can be made.

        >>> dishes = [["pasta", "tomato sauce", "chicken", "garlic", "cheese"],
                      ["chicken curry", "chicken", "curry"],
                      ["nachos", "chicken", "cheese", "chips", "tomatoes"]]
        [['cheese', 'pasta', 'nachos'], ['chicken', 'pasta', 'chicken curry', 'nachos']]

    """

    ingreds = {}
    for i in range(len(dishes)):
        for j in range(1, len(dishes[i])):
            ingreds[dishes[i][j]] = ingreds.get(dishes[i][j], [])
            ingreds[dishes[i][j]].append(dishes[i][0])

    common_ingreds = []
    for ingred, dish_list in ingreds.iteritems():
        if len(dish_list) >= 2:
            common_ingreds.append([ingred] + dish_list)

    return common_ingreds


print get_dishes_by_ingredient(dishes)
