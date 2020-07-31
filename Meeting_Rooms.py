def solve(A):
    count = 1
    length = len(A)
    box = []
    A = sorted(A,key = lambda x:(x[0],x[1]))
    box.append(A[0][1])
    for i in range(1,length):
        if A[i][0] < min(box):
            count += 1
            box.append(A[i][1])
        elif A[i][0] >= min(box):
            box[box.index(min(box))] = A[i][1]
    return count
                
            