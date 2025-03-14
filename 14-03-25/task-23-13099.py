def f(cur, end, A=False):
    if cur == end:
        return 1
    if cur > end + 1:
        return 0
    if A:
        return f(cur * 2, end) + f(cur * 3, end)
    return f(cur - 1, end, True) + f(cur * 2, end) + f(cur * 3, end)

print(f(3, 15))