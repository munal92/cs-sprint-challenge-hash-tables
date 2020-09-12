def intersection(arrays):
    main_arr_length = len(arrays)
    # print(f'arr length -> {main_arr_length}\n')
    store = {}
    if main_arr_length > 1:
        store = dict.fromkeys(arrays[0], 1)
        for i in range(1, len(arrays)):
            for j in arrays[i]:
                if j in store:
                    store[j] += 1

    return list(dict(filter(lambda x: x[1] == main_arr_length, store.items())).keys())


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
