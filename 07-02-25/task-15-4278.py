def f(A):
    for x in range(1, 1000):
        return (A % 12 == 0) and ((530 % x == 0) <= (not A % x == 0) <= (not 170 % x == 0))

count = 0
for A in range(1, 1001):
    if f(A):
        count += 1
print(count)