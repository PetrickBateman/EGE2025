from ipaddress import ip_network

for mask in range(16, 25):
    net = ip_network(f'127.63.67.1/{mask}', False)
    for i in net:
        i = f'{int(i):032b}'
        if i[:16].count('1') < i[16:].count('1'):
            break
    else:
        print(net.netmask)
        break