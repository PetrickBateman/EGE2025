from itertools import product

alph = '0123456789AB'

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 1:
        val = [val.replace(i, '*') for i in '9AB']
        val = ''.join(val)
        if val.count('*') <= 3:
            count += 1

print(count)