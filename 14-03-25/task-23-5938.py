def f(cur, end, cnt=0):
    if cur == end and cnt == 51:
        return 1
    if cur > end:
        return 0
    return f(cur * 4, end, cnt+1) + f(cur + 1, end, cnt+1) + f(cur * 3, end, cnt+1)

print(f(2, 404))