import socket
import re
from common_ports import ports_and_services

# Determine if a string is an IPv4 or a Hostname
def check_ip_addr(target):
    reg = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    if reg.search(target):
        # IPv4
        return True
    else:
        # Host
        return False

# Determine if an IPv4 is valid
def check_ip_valid(target):
    reg = re.compile(r'([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})')
    result = reg.search(target)
    oct1 = int(result.group(1))
    oct2 = int(result.group(2))
    oct3 = int(result.group(3))
    oct4 = int(result.group(4))
    if oct1 >= 1 and oct1 <= 255 and oct2 >= 1 and oct2 <= 255 and oct3 >= 1 and oct3 <= 255 and oct4 >= 1 and oct4 <= 255:
        # IPv4 is valid
        return True
    else:
        # IPv4 is invalid
        return False

# Main Function
def get_open_ports(target, port_range, bool = False):
    open_ports = []

    try:
        if check_ip_addr(target):
            if check_ip_valid(target):
                host = socket.gethostbyaddr(target)[0]
                addr = target
            else:
                result = "Error: Invalid IP address"
                return result
        else:
            host = target
            addr = socket.gethostbyname(target)
    except socket.herror:
        host = ''
        addr = target
    except socket.gaierror:
        result = "Error: Invalid hostname"
        return result

    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        status = sock.connect_ex((host, port))
        if status == 0:
            open_ports.append(port)
        sock.close()

    if bool == False:
        return open_ports
    else:
        result = ''
        if host != '':
            result += f'Open ports for {host} ({addr})\n'
        else:
            result += f'Open ports for {addr}\n'
        result += f'PORT     SERVICE\n'
        for i in open_ports:
            name = ports_and_services[i]
            temp = str(i).ljust(9)
            result += f'{temp}{name}\n'
        return result[:-1]
