import socket

def get_open_ports(target, port_range, bool = False):
    open_ports = []

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    for port in range(port_range[0], port_range[1]):
        status = sock.connect_ex((target, port))
        if status == 0:
            open_ports.append(port)
            sock.close()

    if not bool:
        return(open_ports)
    else:
        print('bool == False')

    #return(open_ports)