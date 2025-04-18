from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'192.214.{A}.184/27', False)
    for i in net:
        i = f'{int(i):032b}'
        if sum(map(int, i)) <= 15:
            break
    else:
        print(A)
        break