def fold_array(a, n):
    b = a[:]
    for i in range(n):
        for i in range(len(b)//2):
            b[i] += b[-i-1]
        b[:] = b[:(len(b)+1)//2]
    return b
