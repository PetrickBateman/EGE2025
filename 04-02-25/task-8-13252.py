from itertools import permutations

alph = ''.join(set('КИДАЛА'))

count = 0
for i in permutations(alph, 5):
    i = ''.join(i)
    for j in i:
        if i[j] != i[j + 1]:
            count += 1
print(count)