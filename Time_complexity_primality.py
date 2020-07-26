def primality(n):
    root = (n**0.5)
    if n == 1:
        return("Not prime")
    if root == int(root):
        end = int(root) + 1
    else:
        end = int(root)
    for i in range(2,end):
        if n%i == 0:
            return("Not prime")
    return("Prime")