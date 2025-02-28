def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return 0
    return True

cnt = 0
for i in range(194441, 196501):
    if is_prime(i) and i % 100 == 93:
        cnt += 1
        print(cnt, i)