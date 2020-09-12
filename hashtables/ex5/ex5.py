# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    store = dict.fromkeys(queries, 1)
    store2 = {}
    for i in files:
        if i.split('/')[-1] in store:
            store2[i] = 1
    return list(store2.keys())


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
