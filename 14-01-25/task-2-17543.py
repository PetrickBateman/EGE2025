from itertools import product, permutations

def f(w, x, y, z):
    return (y <= (not(x <= z))) or w

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = (
        (a1, 0, a2, a3),
        (0, 1, a4, a5),
        (1, a6, a7, 0)
    )
    for p in permutations('wxyz'):
        u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
        if u:
            print(*p)