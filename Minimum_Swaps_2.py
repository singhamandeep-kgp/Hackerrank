def minimumSwaps(arr):
    count = 0
    new_arr = arr.copy()
    new_arr.sort()
    length = len(arr)
    for i in range(0,length):
        focus_var = new_arr[i]
        for j in range(0, length):
            if focus_var == arr[j] and i != j:
                temp = arr[i] 
                arr[i] = arr[j]
                arr[j] = temp
                count += 1
    return(count)
        

