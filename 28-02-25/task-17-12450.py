with open('17_12450.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if i % 52 == 0)
ans = []

for i in range(len(data) - 2):
    n1, n2, n3 = data[i:i+3]
    nums = [n1, n2, n3]
    if sum(i % 113 for i in nums) == minn:
        ans.append(sum(nums))

print(len(ans), max(ans))