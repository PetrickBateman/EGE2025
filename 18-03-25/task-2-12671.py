from itertools import product, permutations

def f(w, x, y, z):
    f = (not(x == (w and (not z))) and (y == (x and (not w))))
    if f:
        return f
    return 0

for a1,a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = (
        (a1, a2, 0, a3),
        (a4, 0, a5, 0),
        (0, a6, 1, 0)
    )
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)