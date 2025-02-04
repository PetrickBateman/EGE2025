from itertools import combinations

def f(x):
    P = 1 <= x <= 39
    Q = 23 <= x <= 58
    A = A1 <= x <= A2
    return (P <= (not Q)) <= (not A)

ans = []
line = [x / 10 for x in range(59 * 10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(max(ans))