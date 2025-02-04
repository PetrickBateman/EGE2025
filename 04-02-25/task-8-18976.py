from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase


count = 0
for val in product(alph[:20], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and int(val[0], 20) + int(val[-1], 20) == 26:
        for i in '02468ACEGIKMOQSUWY':
            val = val.replace(i, '*')
        for i in '13579BDFHJLNPRTVXZ':
            val = val.replace(i, '&')
        if '**' not in val and '&&' not in val:
            count += 1

print(count)