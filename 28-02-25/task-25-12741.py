from itertools import product

ans = []

for r in range(8):
    for R in range(8 - r):
        for x in product('0123456789', repeat=r):
            for X in product('0123456789', repeat=R):
                x = ''.join(x)
                X = ''.join(X)
                num = int(f'4{x}5{X}6')
                if num < 10 ** 10 and num % 1234 == 0:
                    ans.append((num, num // 1234))


for r in range(5):
        for x in product('0123456789', repeat=r):
            for y in '123456789':
                for z in '0123456789':
                    x = ''.join(x)
                    num = int(f'{y}74{x}68{z}')
                    if num < 10 ** 10 and num % 1234 == 0:
                        ans.append((num, num // 1234))

ans = sorted(ans)
for i in ans[::-1]:
    print(*i)