# ICMP Spoofing and Sniffing Scripts

## Overview

This repository contains three Python scripts for spoofing and sniffing ICMP (Internet Control Message Protocol) packets using the Scapy library. These scripts are intended for educational and testing purposes only, demonstrating how network packets can be intercepted and spoofed.

### Scripts

1. **icmp_spoof.py**: This script sends a spoofed ICMP packet to a specified destination.
2. **sniff_spoof_icmp.py**: This script sniffs ICMP echo request packets and sends a spoofed ICMP echo reply in response.
3. **sniffer.py**: This script sniffs ICMP packets on a specified network interface and prints out packet details.

## Requirements

- Python 3.x
- Scapy library

To install Scapy, run:
```bash
pip install scapy
```

## Usage

### 1. ICMP Spoofing

**Script**: `icmp_spoof.py`

This script sends a spoofed ICMP packet from a fake source IP to a specified destination.

#### How to run:

```bash
python3 icmp_spoof.py
```

### 2. Sniff and Spoof ICMP

**Script**: `sniff_spoof_icmp.py`

This script listens for ICMP echo request packets from a specific IP address and sends back spoofed ICMP echo replies.

#### How to run:

```bash
python3 sniff_spoof_icmp.py
```

### 3. ICMP Packet Sniffer

**Script**: `sniffer.py`

This script sniffs ICMP packets on a network interface and prints the source IP, destination IP, and protocol.

#### How to run:

```bash
python3 sniffer.py
```

### Notes

- Ensure you have the necessary permissions to run network sniffing scripts on your machine.
- Replace `iface` in `sniffer.py` with your network interface name if needed.
