def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return 0
    return True

count = 0
for i in range(600_001, 10**20):
    sosed1 = i-1
    sosed2 = i+1
    if i % 6 == 0:
        if is_prime(sosed1) and is_prime(sosed2):
            print(sosed1, sosed2)
            count += 1
            if count == 6:
                break
