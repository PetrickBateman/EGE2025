def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): res.add(i)
            if is_prime(num // i): res.add(num // i)

    res = sorted(res)

    if len(res) >= 2:
        M = min(res) + max(res)
        if (M > 2000) and (M % 10 == 8):
            return M
    return 0

count = 0
for i in range(1_200_001, 10**20):
    res = f(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break