def insertionSort2(n, arr):

    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if arr[j+1] < arr[j]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        for i in arr:
            print(i, end = " ")
        print("\r")
        
    
            
            