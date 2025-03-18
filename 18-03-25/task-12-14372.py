def prime(num):
    if num < 1:
        return 0
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return 0
    return num


for n in range(4, 10000):
    s = '>' + '0' * 25 + '1' * n + '2' * 25
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>')
        if '>2' in s:
            s = s.replace('>2', '2>')
        if '>0' in s:
            s = s.replace('>0', '1>')
    s = s.replace('>', '')
    if prime(sum(map(int, s))):
        print(n)
        break