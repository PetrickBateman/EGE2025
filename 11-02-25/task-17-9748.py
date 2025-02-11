with open('17_9748.txt') as file:
    data = [int(i) for i in file]

ans = []
count = 0
maxx = max(i for i in data if str(i)[-2:] == '15')
for i in range(len(data) - 2):
    num1, num2, num3 = data[i], data[i + 1], data[i + 2]
    nums = [num1, num2, num3]
    u1 = [len(str(i)) for i in nums].count(4) == 1
    u2 = sum(nums) >= maxx
    if u1 and u2:
        count += 1
        ans.append(num1 + num2 + num3)

print(count, max(ans))