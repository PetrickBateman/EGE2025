with open ('17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)
l = []
count = 0
for i in range(len(data) - 1):
    if data[i] % 117 == minn or data[i + 1] % 117 == minn:
        count += 1
        l.append(data[i] + data[i + 1])

print(count, max(l))