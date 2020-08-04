import statistics
class Solution:
    # @param A : string
    # @return an integer
    def seats(self,A): 
        A = list(A)
        length_A = len(A)
        x = []
        count = 0
        MOD = 10000003
        for i in range(0,len(A)):
            if A[i] == "x":
                x.append(i)
        if len(x) == 0:
            return 0
        else:
            median = statistics.median(x)
            length = len(x)
        for i in range(int(median),-1,-1):
            if A[i] == ".":
                for j in range(i,-1,-1):
                    if A[j] == "x":
                        count += abs(i-j)
                        A[j] = "."
                        A[i] = "x"
                        break
        for i in range(int(median)+1,length_A):
            if A[i] == ".":
                for j in range(i,length_A):
                    if A[j] == "x":
                        count += abs(j-i)
                        A[j] = "."
                        A[i] = "x"
                        break
        return count%MOD