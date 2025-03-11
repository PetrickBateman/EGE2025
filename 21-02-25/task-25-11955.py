from itertools import product
ans = []
for r in range(4):
    for i in product('13579', repeat=r):
        for j in '02468':
            i = ''.join(i)
            num = int(f'1{j}2157{i}4')
            if num % 133 == 0 and num < 10**10:
                ans.append([num, num // 133])
for i in sorted(ans):
    print(*i)