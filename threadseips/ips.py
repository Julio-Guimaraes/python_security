import ipaddress

ip = "192.168.0.0/16"

rede = ipaddress.ip_network(ip, strict=False)
for ip in rede:
    print(ip)