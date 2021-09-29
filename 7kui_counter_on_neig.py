def ones_counter(inp):
    count = 0
    res = []
    for i in inp:
        if i == 1:
            count += 1
        if i == 0 and count != 0:
            res.append(count)
            count = 0
    if count != 0:
        res.append(count)
    return res


# def ones_counter(input):
#     return [i.count('1') for i in ''.join(map(str, input)).split('0') if i]


print((ones_counter([0]), []))
print((ones_counter([1, 0, 1, 1]), [1, 2]))
print((ones_counter([0, 0, 0, 0, 0, 0, 0, 0]), []))
print((ones_counter([1, 1, 1, 1, 1]), [5]))
print((ones_counter([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]), [3, 1, 2]))
print((ones_counter([0, 0, 0, 1, 0, 0, 1, 1]), [1, 2]))
print((ones_counter([1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]), [1, 2, 4, 1]))
