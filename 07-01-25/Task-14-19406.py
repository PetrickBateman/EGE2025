
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[1:35][::-1]:
    num1 = int(f'6{x}QR{x}', 35)
    num2 = int(f'{x}59SH', 35)
    num3 = int(f'PH{x}69YW', 35)
    num = num1 + num2 + num3
    maxx = 0
    let = 0
    for i in digits:
        str(num).count(i)
        if str(num).count(i) >= maxx:
            maxx = str(num).count(i)
            let = int(i)
    if num % let ** 2 == 0:
        print(num // let ** 2)
        #ans: 46865133191