import socket

def get_open_ports(target, port_range, bool = False):
    open_ports = []

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    for port in range(port_range[0], port_range[1]):
        if sock.connect_ex((target, port)) == 0:
            open_ports.append(port)
            sock.close()

    if bool:
        print('bool == True')
    else:
        print('bool == False')

    return(open_ports)