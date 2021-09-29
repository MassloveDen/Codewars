def xmastree(n):
    # complete this code
    res = []
    ins = ''
    len = 2 * n + 1
    for i in range(1, n+1):
        ins = '_' * (len//2-i) + '#' * (2*i-1) + '_' * (len//2-i)
        res.append(ins)
    res.append('_' * (len // 2 - 1) + '#' * (2 * 1 - 1) + '_' * (len // 2 - 1))
    res.append('_' * (len // 2 - 1) + '#' * (2 * 1 - 1) + '_' * (len // 2 - 1))
    return res

def xMasTree(n):
    hashtags = '#' * (n - 1)
    spaces = '_' * (n - 1)
    tree = []
    for i in range(n):
        left = spaces[i:] + hashtags[:i]
        tree.append(left + '#' + left[::-1])
    for i in range(2):
        tree.append(spaces + '#' + spaces)
    return tree


print(xmastree(3))