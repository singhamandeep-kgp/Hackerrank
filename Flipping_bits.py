def flippingBits(n):
    val = 0
    bla = []
    remainder = n
    for i in range(31,-1,-1):
        decimal_val = (2**i)
        if remainder < decimal_val:
            bla.append(1)
        elif remainder >= decimal_val:
            remainder = remainder%decimal_val
            bla.append(0)
    for count,item in enumerate(bla):
        if item == 1:
            val += 2**(31-count)
    return val 