def prime(n):
    if n < 2:
        return 0
    res = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return 0
    return 1


def f(n):
    res = set()
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            res |= {i, n // i}

    if len(res) > 2:
        M = sum(res)
        if prime(M % 100_000):
            return M
    return 0

count = 0
for i in range(1_273_548, 10**20):
    M = f(i)
    if M:
        print(i, M)
        count += 1
        if count == 5:
            break