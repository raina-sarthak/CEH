import pscan

targets_ip = input('Enter the target to scan: ')
port_num = int(input('Amount of ports to scan: '))
vul_file = input("Enter path to the file with vunerable software: ")
print('\n')

target = pscan.PortScan(targets_ip,port_num)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] Vunerable banner: "' + banner + '" On port: "' + str(target.open_ports) + 'found.')
    count += 1

