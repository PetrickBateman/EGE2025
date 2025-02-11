with open('17_9786.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(i)[-2:] == '25')

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    nums = [num1, num2, num3]
    u1 = [len(str(abs(i))) for i in nums].count(4) <= 2
    u2 = sum(nums) <= maxx
    if u1 and u2:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))