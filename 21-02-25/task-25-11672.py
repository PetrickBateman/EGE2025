from fnmatch import fnmatch

for i in range(123405 - 123405 % 21025, 10**10, 21025):
    f = str(i)
    if fnmatch(str(i), '12*34?5'):
        for j in '24680':
            s = [j for j in str(i) if j in '24680']
        s = ''.join(s)
        if len(s) - s.count('*') == s.count('*'):
            print(i, i // 21025)