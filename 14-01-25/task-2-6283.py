from itertools import product, permutations

def f(w, x, y, z):
    return (not (not (x <= (not w))) and z) and not (w <= z) and (x <= (not z))

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = (
        (1, 0, a1, 0),
        (1, 0, a2, a3),
        (a4, 1, a5, 1)
    )
    for p in permutations('wxyz'):
        u = [f(**dict(zip(p, t))) for t in table] == [1, 0 ,0]
        if u:
            print(*p)