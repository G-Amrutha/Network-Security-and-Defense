#!/usr/bin/env python3
import scapy.all as scapy

def spoof_icmp_response(pkt):
    """Spoofs an ICMP response packet from the intended destination.

    Args:
        pkt: The ICMP echo request packet to spoof a response for.

    Returns:
        A spoofed ICMP echo reply packet.
    """

    # Create a new IP packet with the source and destination IPs swapped.
    ip = scapy.IP(src=pkt[scapy.IP].dst, dst=pkt[scapy.IP].src)

    # Create a new ICMP echo reply packet.
    icmp = scapy.ICMP(type=0, code=0, id=pkt[scapy.ICMP].id, seq=pkt[scapy.ICMP].seq)

    # Create a new packet with the IP and ICMP headers.
    newpkt = ip/icmp

    # Send the spoofed packet.
    scapy.send(newpkt)

def main():
    """Sniffs ICMP packets sent from 10.9.0.1 and spoofs a response from the intended destination."""

    # Filter for ICMP echo request packets sent from 10.9.0.1.
    filter = "icmp and host 10.9.0.1"

    # Sniff ICMP packets and spoof responses.
    scapy.sniff(filter=filter, prn=spoof_icmp_response)

if __name__ == "__main__":
    main()