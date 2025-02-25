def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    P = [i for i in res if is_prime(i)]
    E = [i for i in res if i % 2 == 0]
    M = abs(sum(P) - sum(E))
    if len(P) == len(E):
        return M
    return 0

count = 0
for i in range(100_000_001, 10**20):
    res = f(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break
