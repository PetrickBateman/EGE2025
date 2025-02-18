from itertools import product

ans = []
for r in range(3):
    for x in product('0123456789', repeat=r):
        for y in product('0123456789', repeat=1):
            x = ''.join(x)
            y = ''.join(y)
            n = int(f'123{x}4{y}5')
            if n < 10 ** 8 and n % 161 == 0:
                ans.append((n, n // 161))

ans = sorted(ans)
for i in ans:
    print(*i)