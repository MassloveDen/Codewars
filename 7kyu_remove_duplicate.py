def remove_duplicate_words(s):
    res = []
    for i in s.split(' '):
        if i not in res:
            res.append(i)
    return ' '.join(i for i in res)
