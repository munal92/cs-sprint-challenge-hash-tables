def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    store = {}
    for index, i in enumerate(weights):
        if limit - i in store:
            indexes = store.get(limit-i), index
            return list(sorted(indexes, reverse=True))
        store[i] = index


# weights = [4, 6, 10, 15, 16]
# length = 5
# limit = 21
# print(get_indices_of_item_weights(weights, length, limit))


"""
    21 - 4 = 17    17:4         
    21 -15 = 6     6:15           
    21 - 16 = 15   15:16        
 """
