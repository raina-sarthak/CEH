import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('/n' + '-_0 Scanning target: ' + str(target))
    for port in range(1,100):
        scan_port(converted_ip,port)

def get_banner(s):
    return s.recv(1024)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress,port))
        try:
            banner = get_banner(sock)
            print('[+] ' +str(port)+ ' connection successful.' + 'banner:' + banner)
        except:
            print('[+] ' +str(port)+ ' connection successful. no banner found')
    except:
        pass


# this next line (line 36) tells python whether this coe is running as a main file or is being imported.
if __name__ == "__main__":
    targets = input('Enter target to scan: ')
    if ',' in targets:
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '))
    else:
        scan(targets)
