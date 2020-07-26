def icecreamParlor(m, arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] < m and arr[j] < m:
                if arr[i] + arr[j] == m:
                    return(i+1,j+1)
