from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase

count_l = 0
for val in product(alph[:15], repeat=5):
    val = ''.join(val)
    ans = 0
    if val[0] != '0' and val.count('8') == 1:
        for i in val:
            if i in ascii_uppercase:
                ans += 1
    if ans >= 2:
        count_l += 1
print(count_l)