def f(cur, end, A=0, B=0, C=0):
    if cur == end and A <= 4 and B >= 2 and C == 5:
        return 1
    if cur > end:
        return 0
    return f(cur * 5, end, A+1, B, C) + f(cur * 3, end, A, B+1, C) + f(cur + 45, end, A, B, C+1)

print(f(1, 2970))