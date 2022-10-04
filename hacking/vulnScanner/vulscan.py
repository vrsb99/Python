import vulnScanner

targets_ip = input('[+] * Enter Target To Scan For Vulnerable Open Ports: ')
port_number = (input('[+] * Enter Amount Of Ports You Want To Scan(500 - first 500 ports): '))
if port_number == "":
    port_number = 100
else:
    port_number = int(port_number)

vul_file = input('[+] * Enter Path To The File With Vulnerable Software: ')
print('\n')

target = vulnScanner.PortScan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:  # 'r' to read from file
    count = 0
    for banner in target.banners:
        file.seek(0)  # Re-read from beginning of file
        for line in file.readlines():  # .readlines to read multiple lines
            if line.strip() in banner:  # Checks if each line in txt file is available in banners
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(target.open_ports[count]))
        count += 1
