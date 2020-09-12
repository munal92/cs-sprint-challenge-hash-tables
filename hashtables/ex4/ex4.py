def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    store = {}
    if len(a) > 0:
        for i in a:
            if abs(i) not in store:
                store[abs(i)] = 1
            elif abs(i) in store:
                store[abs(i)] += 1
        return list(dict(filter(lambda x: x[1] == 2, store.items())).keys())


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
