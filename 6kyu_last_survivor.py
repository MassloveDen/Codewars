def last_survivors(string):
    ans = list(string)
    abc = list(map(chr, range(97, 123)))  # all letters
    abc.append('a')  # append the first letter at last z - a - b ...

    for f in range(len(string)):
        for i in ans:
            if ans.count(i) >= 2:
                index = abc.index(i)
                ans.remove(i)
                ans.remove(i)
                ans.append(abc[index + 1])

    return "".join(ans)
