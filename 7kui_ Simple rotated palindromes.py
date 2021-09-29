def solve(st):
    for _ in st:
        st = st[-1] + st[:-1]
        if is_palindrome(st):
            return True
    return False


def is_palindrome(s):
    return s == s[::-1]


print(solve("aaab"))
print(solve("abcabc"))
print(solve("4455"))
print(solve("zazcbaabc"))
print(solve("223456776543"))
print(solve("432612345665"))
print(solve("qponmlkjihgfeeiefghijklmnopqrsttsr"))
