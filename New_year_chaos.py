def minimumBribes(q):
    
    n = len(q)
    count = 0
    bla = 0


    def swap(array, pos1, pos2, temp):
        temp = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = temp

    pri = True

    for i in range(n - 1, - 1, - 1):
        if q[i] != i + 1:
            if q[i - 1] == i + 1:
                swap(q, i - 1, i, bla)
                count += 1
            elif q[i-2] == i + 1:
                swap(q, i - 2, i - 1, bla)
                swap(q, i - 1, i, bla)
                count += 2
            else:
                pri = False
                print("Too chaotic")
                break
    if pri:
        print(count)

