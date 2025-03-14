with open('17_14952.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(i)[-3:] == '121')
ans = []

for i in range(len(data) - 2):
    nums = data[i:i+3]
    u1 = sum([1 for i in nums if len(str(abs(i))) == 4 and i % 2 == 0]) <= 1
    u2 = sum(nums) <= maxx
    if u1 and u2:
        ans.append(sum(nums))

print(len(ans), max(ans))