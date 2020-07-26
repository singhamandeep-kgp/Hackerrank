def runningTime(arr):
    count = 0 
    n = len(arr)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                count += 1
    return count