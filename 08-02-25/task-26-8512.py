with open('input.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

cnt = 0
data = sorted(data)
cells = [0] * K
last_cell = 0

for start, end in data:
    for i in range(len(cells)):
            if cells[i] < start:
                cells[i] = end
                cnt += 1
                last_cell = i + 1
                break

print(last_cell, cnt)

#ans: 133, 389