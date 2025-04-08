with open('17.txt') as file:
    data = [int(i) for i in file]

summ = sum(i for i in data if i < 0)
ans = []

for i in range(len(data) - 2):
    nums = data[i:i+3]
    u1 = max(nums) * min(nums) > summ
    if u1:
        ans.append(sum(nums))

print(len(ans), abs(max(ans)))