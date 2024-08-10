# Network Security Testing Scripts

## Overview

This repository contains various scripts designed for network security testing and educational purposes. These scripts demonstrate concepts such as packet sniffing, spoofing, session hijacking, SYN flooding, and TCP reset attacks.

### Scripts

1. **icmp_spoof.py**: Sends a spoofed ICMP packet to a specified destination.
2. **sniff_spoof_icmp.py**: Sniffs ICMP echo request packets and sends a spoofed ICMP echo reply.
3. **sniffer.py**: Sniffs ICMP packets on a specified network interface and prints packet details.
4. **sessionhijack.py**: Performs a session hijacking attack by spoofing TCP packets.
5. **reset.py**: Executes a TCP reset attack by sending forged TCP reset packets.
6. **synflood.py**: Launches a SYN flood attack using Python to overwhelm a target with TCP SYN packets.
7. **synflood.c**: A C program that also performs a SYN flood attack on a specified target.

## Requirements

- Python 3.x
- Scapy library (for Python scripts)
- GCC compiler (for compiling the C program)

To install Scapy, run:
```bash
pip install scapy
```

To compile the C program, use:
```bash
gcc -o synflood synflood.c
```

## Usage

### ICMP Spoofing

**Script**: `icmp_spoof.py`

This script sends a spoofed ICMP packet from a fake source IP to a specified destination.

#### How to run:

```bash
python3 icmp_spoof.py
```

### Sniff and Spoof ICMP

**Script**: `sniff_spoof_icmp.py`

This script listens for ICMP echo request packets from a specific IP address and sends back spoofed ICMP echo replies.

#### How to run:

```bash
python3 sniff_spoof_icmp.py
```

### ICMP Packet Sniffer

**Script**: `sniffer.py`

This script sniffs ICMP packets on a network interface and prints the source IP, destination IP, and protocol.

#### How to run:

```bash
python3 sniffer.py
```

### Session Hijacking

**Script**: `sessionhijack.py`

This script performs a session hijacking attack by spoofing TCP packets to inject data into an existing TCP session.

#### How to run:

```bash
python3 sessionhijack.py <client_ip> <server_ip>
```

### TCP Reset Attack

**Script**: `reset.py`

This script performs a TCP reset attack by sending forged TCP reset packets to terminate a TCP connection.

#### How to run:

```bash
python3 reset.py <client_ip> <server_ip>
```

### SYN Flood Attack (Python)

**Script**: `synflood.py`

This script launches a SYN flood attack by sending numerous TCP SYN packets to a target, aiming to exhaust its resources.

#### How to run:

```bash
python3 synflood.py
```

### SYN Flood Attack (C)

**Program**: `synflood.c`

This C program performs a SYN flood attack, similar to the Python version, but using a compiled executable.

#### How to compile and run:

```bash
gcc -o synflood synflood.c
./synflood <target_ip> <target_port>
```

### Notes

- Ensure you have the necessary permissions to run network sniffing and spoofing scripts on your machine.
- Replace `iface` in the Python scripts with your network interface name if needed.
- Use these scripts only in controlled environments with explicit permission, as unauthorized use is illegal and unethical.
