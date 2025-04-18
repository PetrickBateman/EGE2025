from ipaddress import ip_network

count = 0
net = ip_network('214.187.224.0/19')
for i in net:
    i = f'{int(i):032b}'
    if sum(map(int, i)) % 6 != 0 and i[-4:] == '1000':
        count += 1
print(count)