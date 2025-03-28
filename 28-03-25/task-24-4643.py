with open('24_4643.txt') as file:
    data = file.readline()

data = data.replace('2', '1')
data = data.replace('A', 'B')
data = data.replace('11B' , '*')
data = data.replace('B', ' ').replace('1', ' ')
data = data.split()
print(max(len(i) for i in data))