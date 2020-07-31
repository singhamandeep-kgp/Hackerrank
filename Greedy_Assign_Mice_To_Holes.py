def mice(self, A, B):
    A.sort()
    B.sort()
    length = len(A)
    bla = []
    for i in range(0,length):
        bla.append(abs(A[i]-B[i]))
    return max(bla)
