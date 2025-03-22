from itertools import groupby

with open('26_4553.txt') as file:
    N = file.readline()
    data = [list(i.split()) for i in file]

m = []
for i in range(10000):
    m.append(["-"] * 10000)

for gor, ver, zn in data:
    m[int(gor)][int(ver)] = zn
# print(m)
ans = []
for i in range(10000):
    posl = [len(list(group)) for symb, group in groupby(m[i]) if symb == '+']
    if posl:
        ans.append([max(posl), i])

print(*max(ans))