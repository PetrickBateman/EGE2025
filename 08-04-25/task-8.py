from itertools import product

alph = sorted('ДГИАШЭ')

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != 'А' and val[0] != 'Э' and val[0] != 'И':
        if val[-1] != 'Д' and val[-1] != 'Г' and val[-1] != 'Ш':
            count += 1

print(count)
