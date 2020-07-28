def gcd(a,b):
    small = int(min(a,b))
    big = int(max(a,b))
    if small == 0:
        return big
    if small == 1:
        return 1
    else:
        return gcd(small,big%small)
