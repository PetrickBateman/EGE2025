def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x - y >= 39) or (y <= x) or (y >= A - 20)
            if not f:
                return False
    return True

for A in range(1, 10000)[::-1]:
    if f(A):
        print(A)
        break