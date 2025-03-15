with open ('26_17537.txt') as file:
    N, M, K = map(int, file.readline().split())
    seats = [list(map(int, i.split())) for i in file]
seats = sorted(seats, key=lambda x: (x[1], -x[0]))

hall = [M + 1] * (K + 1)
for r, m in seats:
    hall[m] = r

ans = []
for i in range(1, K):
    r1, r2 = hall[i:i+2]
    ans.append([min(r1, r2) - 1, i + 1])

print(max(ans))
