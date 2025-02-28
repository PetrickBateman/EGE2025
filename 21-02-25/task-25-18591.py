from itertools import product

ans = []
for r in range(3):
    for R in range(3):
        for x in product('0123456789', repeat=r):
            for X in product('0123456789', repeat=R):
                x = ''.join(x)
                X = ''.join(X)
                num = int(f'124{x}5{X}79')
                num2 = str(num)
                for i in '02468':
                    num2 = num2.replace(i, '')
                if num % sum(map(int, num2)) == 0 and r + R <= 2:
                    ans.append([num, sum(map(int, str(num)))])
ans = sorted(ans)
for j in ans:
    print(*j)