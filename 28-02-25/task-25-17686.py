def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    for i in res:
        if i % 10 == 7 and i != 7:
            return i
    return 0

count = 0
for i in range(700001, 10**20):
    res = f(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break


