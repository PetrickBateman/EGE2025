from ipaddress import ip_network, ip_address

ip1 = ip_address('193.175.175.231')
ip2 = ip_address('193.175.176.118')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address != net2.network_address:
        if ip1 not in (net1.network_address, net1.broadcast_address):
            if ip2 not in (net2.network_address, net2.broadcast_address):
                print(net1.netmask)