# -*- coding: utf-8 -*-
def x(n):
    # have fun ;)
    res = []
    for i in range(n // 2):
        res.append('□' * i + '■' + '□' * (n - 2 * i - 2) + '■' + '□' * i)
    res.append('□'*(n//2) + '■' + '□'*(n//2))
    for i in range(n // 2 + 1, 1, -1):
        res.append('□' * (i - 2) + '■' + '□' * (n - 2 * i + 2) + '■' + '□' * (i - 2))
    ans = ''.join([x +'\n' for x in res])
    print(ans[:-2])
    return 1


# def x(n):
#     matrix = [list('□'*n) for _ in range(n)]
#     for i in range(n):
#         matrix[i][i] = '■'
#         matrix[i][i*(-1)-1] = '■'
#     return '\n'.join([''.join(series) for series in matrix])


# def x(n):
#     ret = [['□' for _ in range(n)] for _ in range(n)]
#     for i in range(len(ret)):
#         ret[i][i] = '■';
#         ret[i][-1 - i] = '■';
#     return '\n'.join(''.join(row) for row in ret)


print(x(7))
