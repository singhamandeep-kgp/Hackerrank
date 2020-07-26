def partition(arr,start,end):
    
    i = start - 1
    pivot = arr[end]

    for j in range(start,end):
        if arr[j] <= pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return (i+1)

def quicksort(arr,start,end):
    if start < end:
        pIndex = partition(arr,start,end)
        quicksort(arr,start,pIndex-1)
        quicksort(arr,pIndex+1,end)

def findMedian(arr):
    quicksort(arr,0,len(arr)-1)
    l = len(arr)
    index = int((l-1)/2)
    return(arr[index])
