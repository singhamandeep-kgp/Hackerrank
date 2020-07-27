import sys

X = int(input())
N = int(input())
# Complete the powerSum function below.
def powerSum(X, N, start_val):
    count = 0
    for i in range(start_val,X):
        ans = X-i**N
        if ans == 0:
            count += 1
        elif ans > 0:
            count += powerSum(ans,N,i+1)
        elif ans < 0:
            continue 
    return count
print(powerSum(X,N,1))



