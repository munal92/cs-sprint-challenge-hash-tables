# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    store = {}

    store = dict.fromkeys(files, 0)
    # for i in dict.keys():
    #     split_version = i.split('/')[-1]
    #     # print(split_version, i)
    #     if split_version in queries:
    #         store[i] = 1
    # # return list(store.keys())
    return list(dict(filter(lambda x: x[0].split('/')[-1] in queries, store.items())).keys())


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
