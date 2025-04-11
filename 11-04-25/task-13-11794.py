from ipaddress import ip_network

for A in range(0, 255):
    net = ip_network(f'223.167.{A}.167/255.255.255.192', False)
    for i in net:
        i = f'{int(i):032b}'
        if i[:16].count('0') > i[16:].count('0'):
            break
    else:
        print(A)