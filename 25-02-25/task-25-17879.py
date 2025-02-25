def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) >= 2:
        M = min(res) + max(res)
        if M % 10 == 4:
            return M
    return 0

count = 0
for i in range(800001, 10 ** 20):
    N = f(i)
    if N:
        print(i, N)
        count += 1
        if count == 5:
            break