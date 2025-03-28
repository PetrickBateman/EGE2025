def f(cur, end):
    if cur == end:
        return 1
    if cur > end or cur == 9:
        return 0
    return f(cur + 1, end) + f(cur * 2, end)

print(f(2, 12) * f(12, 42))