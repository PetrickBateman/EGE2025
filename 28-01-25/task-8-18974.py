from itertools import product
from string import ascii_uppercase, digits

count = 0
nech = '13579BDFHJLNPRTVXZ'
alph = digits + ascii_uppercase
for val in product(alph[:25], repeat=4):
    val = ''.join(val)
    for i in nech:
        val = val.replace(i, '*')
    if val[0] != '0' and val.count('*') == 1:
        count += 1
print(count)