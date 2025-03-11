def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if i % 2 != 0: res.add(i)
            if (num // i) % 2 != 0: res.add(num // i)
    res = sorted(res)
    if len(res) >= 6:
        return res[-6]
    return 0

ans = []
count = 0
for i in range(200_000_001, 10**20):
    res = f(i)
    if res:
        count += 1
        ans.append([i, res])
        if count == 5:
            break

ans = sorted(ans)
for i in ans:
    print(*i)