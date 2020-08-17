def biggerIsGreater(w):
    arr = list(w)
    for i in range(len(arr)-2,-1,-1):
        for j in range(i+1,len(arr)):
            minimum = arr[i+1]
            if arr[j] <= minimum and arr[j] > arr[i]:
                mini = j
        if minimum > arr[i]:
            temp = arr[i]
            arr[i] = arr[mini]
            arr[mini] = temp
            print(arr)
            arr[i+1: ] = arr[len(arr) - 1 : i : -1]
            return("".join(l for l in arr))
    return("no answer")


