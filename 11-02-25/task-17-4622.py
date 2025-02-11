with open('17_4622.txt') as file:
    data = [int(i) for i in file]

minn = []

for i in data:
    if i > 0 and i % 19 == 0:
        minn.append(i)


ans = []

for i in range(len(data) - 1):
    num1, num2 = data[i], data[i + 1]
    if (num1 + num2) < min(minn):
        ans.append(num1 + num2)

print(len(ans), abs(max(ans)))