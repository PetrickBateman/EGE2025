with open('17_17636.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if len(str(abs(i))) == 3 and abs(i) % 10 == 3)
ans = []
for i in range(len(data) - 2):
    nums = data[i:i+3]
    u1 = sum((1 for i in nums if len(str(abs(i))) == 3 and abs(i) % 10 == 3)) >= 1
    u2 = sum(nums) < maxx
    if u1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))