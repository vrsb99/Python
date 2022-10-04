import socket
from IPy import IP


def scan(target, ports):
    converted_ip = check_ip(target)  # Checks and converts domain to IP
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range(1, ports):  # Range of ports to be scanned
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)  # Gets IP of website


def get_banner(s):
    return s.recv(1024)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()  # Start
        sock.settimeout(0.5)  # Increase value or remove for increase in accuracy
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)  # Receive 1024 bytes of data from IP
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))  # Decodes from bytes
            print('[0_- Scanning in progress]')
        except:
            print('[+] Open Port ' + str(port))
            print('[0_- Scanning in progress]')
    except:
        pass


if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan(split multiple targets with ,): ')
    port_num = input('[+] Enter the number of ports that you want to scan (optional) : ')
    if port_num == "":
        port_num = "500"
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '), int(port_num))
    else:
        scan(targets, int(port_num))
