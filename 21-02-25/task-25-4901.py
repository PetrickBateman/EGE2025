from itertools import product

ans= []
for r in range(4):
    for R in range(4 - r):
        for x in product('0123456789', repeat=r):
            for X in product('0123456789', repeat=R):
                for y in '123456789':
                    for z in '0123456789':
                        x = ''.join(x)
                        X = ''.join(X)
                        num = int(f'{y}6{x}6{X}{z}6')
                        if num % 6 == 0 and num % 7 == 0 and num % 8 == 0:
                            summ = []
                            for i in range(1, num):
                                if num % i == 0:
                                    summ.append(i)
                            ans.append([num, sum(summ)])
ans = sorted(ans)
for i in ans[:7]:
    print(*i)