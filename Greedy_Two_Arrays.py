def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse = True)
    print(A,B)
    length = len(A)
    for i in range(0,length):
        if A[i] + B[i] < k:
            return("NO")
    return("YES")

twoArrays(10,[2,1,3],[7,8,9])