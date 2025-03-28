with open('17_12735.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if i % 100 == 9)
ans = []

for i in range(len(data) - 2):
    nums = data[i:i+3]
    u1 = sum(1 for i in nums if i % 7 == 0) == 2
    u2 = sum(nums) < maxx
    if u1 and u2:
        ans.append(nums[0] * nums[1] * nums[2])
print(len(ans), min(ans))