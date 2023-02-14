import socket
import re
from common_ports import ports_and_services

# Determine if a string is an IPv4 or a Hostname
def check_ip_addr(str):
    reg = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    
    if reg.search(str):
        return True # IPv4
    else:
        return False # Hostname

# Main Function
def get_open_ports(target, port_range, bool = False):
    open_ports = []
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    if check_ip_addr(target):
        try:
            host = socket.gethostbyaddr(target)[0]
            addr = target
        except:
            result = "Error: Invalid IP address"
            return result
    else:
        try:
            host = target
            addr = socket.gethostbyname(target)
        except socket.gaierror as e:
            result = "Error: Invalid hostname"
            return result
    
    for port in range(port_range[0], port_range[1]):
        status = sock.connect_ex((host, port))
        if status == 0:
            open_ports.append(port)
            sock.close()

    if not bool:
        return(open_ports)
    else:
        result = ''
        result += f'Open ports for {host} ({addr})\n'
        result += f'PORT     SERVICE\n'
        for i in open_ports:
            name = ports_and_services[i]
            result += f'{port}       {name}\n'
        return result[:-1]