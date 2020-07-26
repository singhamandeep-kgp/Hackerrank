def countingSort(arr):
    my_dict = {}

    for i in range(0,100):
        my_dict[i] = 0
    for i in arr:
        my_dict[i] += 1

    return my_dict.values()
