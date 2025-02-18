from itertools import product

ans = []
for r in range(3):
    for x in product('0123456789', repeat=r):
        for y in '0123456789':
            for z in '0123456789':
                x = ''.join(x)
                n = int(f'3{y}12{z}14{x}5')
                if n < 10**10 and n % 1917 == 0:
                    ans.append((n, n // 1917))
ans = sorted(ans)
for i in ans:
    print(*i)
