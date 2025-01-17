from itertools import product
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
count = 0

for val in product(alph[:16], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 2:
        for i in '0248ACE':
            val = val.replace(i, '*')
        if '*6' not in val and '6*' not in val and '66' not in val:
            count += 1

print(count)