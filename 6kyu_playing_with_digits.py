def dig_pow(n, p):
    res = 1
    total = 0
    for i in str(n):
        res = int(i)**p
        p += 1
        total += res
    if total % n == 0:
        return total / n
    else:
        return -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))