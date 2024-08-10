#!/usr/bin/env python3
from scapy.all import *

print("SNIFFING PACKETS.........")

def print_pkt(pkt):                       
   print("Source IP:", pkt[IP].src)
   print("Destination IP:", pkt[IP].dst)
   print("Protocol:", pkt[IP].proto)
   print("\n")
   #pkt.show()

pkt = sniff(iface='br-c6e030c4c9e7',filter='icmp',prn=print_pkt)   
