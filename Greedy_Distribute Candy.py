class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        candies = 1
        length = len(A)
        array = [1 for i in range(length)]
        for i in range(1,length):
            if A[i] > A[i-1]:
                array[i] = array[i-1] + 1
        for i in range(length-2,-1,-1):
            if A[i] > A[i+1] and array[i] <= array[i+1]:
                array[i] = array[i+1] + 1
        return sum(array)    