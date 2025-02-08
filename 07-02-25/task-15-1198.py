from itertools import combinations

def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = A1 <= x <= A2
    return (B <= A) and ((not C) or A)

ans = []
line = [x / 10 for x in range(16 * 10, 52 * 10)]

for A1, A2 in combinations(line, 2):
    if not all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))