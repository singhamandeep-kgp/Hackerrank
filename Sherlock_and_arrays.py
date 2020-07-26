def balancedSums(arr):
    
    lsum = 0
    rsum = 0 

    rsum = sum(arr)

    for i in arr:
        rsum -= i 
        if lsum == rsum:
            return "YES"
        lsum += i
    return "NO"
    
    return str(rsum)
    