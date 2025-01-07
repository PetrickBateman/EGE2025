for x in range(1, 5556)[::-1]:
    num = 5**150 + 5**135 - x
    count = 0
    while num:
        if num % 5 == 4:
            count += 1
        num //= 5
    if count == 134:
        print(x)
        break
