with open('17_19486.txt') as file:
    data = [int(i) for i in file]

maxx = [1 for i in data if str(i)[-1] == '7']
maxx = len(maxx)

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    u1 = ((str(num1)[0] == '-') + (str(num2)[0] == '-')) == 1
    u2 = (num1 + num2) <= maxx
    if u1 and u2:
        ans.append(num1 + num2)

print(len(ans), max(ans))
