def f1(s):
    count = [s.count(i) for i in s]
    if count.count(3) == 6 and count.count(1) == 1:
        return 1
    return 0

def f2(s):
    maxx = [i for i in s if s.count(i) > 1]
    minn = [i for i in s if s.count(i) == 1]
    if max(maxx) > minn[0]:
        return 1
    return 0


with open('9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)