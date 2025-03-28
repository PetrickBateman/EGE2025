from itertools import combinations

with open('17 (2)_7718.txt') as file:
    data = [int(i) for i in file]

ans = []
for num1, num2 in combinations(data, 2):
    u1 = (num1 + num2) % 18 == 0
    u2 = num1 * num2 % 18 == 0
    if u1 + u2 == 1:
        ans.append(num1 + num2)

print(len(ans), max(ans))