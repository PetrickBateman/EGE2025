def convert(n, s):
    res = ''
    while n:
        res += str(n % s)
        n //= s
    return res[::-1]

l = []
for n in range(11, 1000):
    r = convert(n, 3)
    if n % 4 == 0:
        r = r + r[-3:]
    else:
        r = '1' + r + '20'
    r = int(r, 3)
    if r > 423:
        l.append(r)
print(min(l))