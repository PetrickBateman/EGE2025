from itertools import product

alph = sorted(set('ПРИВЫЧКА'))

count = 0
for pos, val in enumerate(product(alph, repeat=5), 1):
    val = ''.join(val)
    count += 1
    if pos % 5 == 0:
        count -= 1
    if 'ВКПЧР' in val:
        print(count)
