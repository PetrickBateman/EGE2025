for n in range(1, 10000):
    r = oct(n)[2:]
    if n % 2 == 0:
        r = r + max(r)
    else:
        r = r + oct(n % 2 * 2)[2:]
    if int(r, 8) < 313:
        break