from fnmatch import fnmatch

for i in range((123405 - 123405 % 161), 10**8, 161):
    if fnmatch(str(i), '123*4?5'):
        print(i, i // 161)