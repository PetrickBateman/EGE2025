def f(B):
    for x in range(1, 1000):
        f = ((bin(x)[2:] and bin(500)[2:] != 0) or (bin(x)[2:] and bin(200) == 0)) <= (not(bin(x)[2:] and bin(B)[2:] == 0))
        if not f:
            return False
    return True

for b in range(1, 10000):
    if f(b):
        print(b)
        break