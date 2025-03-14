def f(cur, cnt=0):
    if cur < 0 and cnt == 13:
        ans.append(cur)
        return 1
    if cnt == 13 and cur >= 0:
        return 0
    return f(cur - 3, cnt + 1) + f(cur * -3, cnt + 1)
ans = []
print(f(333), len(set(ans)))