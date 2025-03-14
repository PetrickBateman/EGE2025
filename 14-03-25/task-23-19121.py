def F(cur,end):
    if cur == end:
        return 1
    if cur < end:
        return 0
    return F(cur - 3, end) + F(cur // 3, end)

print(F(35, 8) * F(8, 1))