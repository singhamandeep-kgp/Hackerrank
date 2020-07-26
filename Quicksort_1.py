def quickSort(array):
    array.reverse()

    i = (-1)

    pivot = array[-1]
    n = len(array)
    
    for j in range(0,n):
        if array[j] <= pivot:
            i += 1
            array[j],array[i] = array[i],array[j]
    array[i+1],array[n-1] = array[n-1],array[i+1]
    
    return array
        

