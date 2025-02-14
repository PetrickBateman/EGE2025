with open('17_7716.txt') as file:
    data = [int(i) for i in file]
ans = []
ch = '02468'
maxx = max(i for i in data if '0' not in str(i) and '2' not in str(i) and '4' not in str(i) and '6' not in str(i) and '8' not in str(i))

for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    nums = [num1, num2]
    for j in ch:
        num11 = str(num1).replace(j, '*')
        num22 = str(num2).replace(j, '*')
        if len(set(num11)) == 1 or len(set(num22)) == 1:
            if sum(nums) >= maxx:
                ans.append(sum(nums))
print(len(ans), max(ans))
