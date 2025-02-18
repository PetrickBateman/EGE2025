from string import digits
from itertools import product
ans = []
for r in range(7):
    for x in product(digits, repeat=r):
        x = ''.join(x)
        n = int(f'1234{x}7')
        if n < 10**12 and n % 141 == 0:
            ans.append((n, n // 141))
ans = sorted(ans)
for i in ans:
    print(*i)