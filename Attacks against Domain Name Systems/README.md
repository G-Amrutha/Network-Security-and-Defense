# DNS Spoofing and Packet Generation Scripts

## Overview

This section contains scripts designed to demonstrate DNS spoofing techniques and to generate DNS query and reply packets. These scripts are intended for educational purposes and illustrate how DNS queries can be intercepted and spoofed to redirect traffic.

### Scripts

1. **send_premade_dns.c**: Sends a premade DNS packet read from a binary file to a target IP address.
2. **generate_dns_query.py**: Generates a DNS query packet and saves it to a file.
3. **generate_dns_reply.py**: Generates a DNS reply packet and saves it to a file.
4. **dns_spoof_authority.py**: Performs DNS spoofing by sending fake authoritative DNS replies.
5. **dns_spoof.py**: Spoofs DNS responses to redirect queries for a specific domain.

## Requirements

- Python 3.x
- Scapy library (for Python scripts)
- GCC compiler (for compiling the C program)
- Root or sudo privileges to execute network manipulation scripts.

To install Scapy, run:
```bash
pip install scapy
```

To compile the C program, use:
```bash
gcc -o send_premade_dns send_premade_dns.c
```

## Usage

### Sending Premade DNS Packets

**Program**: `send_premade_dns.c`

This C program reads a premade DNS packet from a binary file and sends it to a target IP address, modifying certain fields before sending.

#### How to compile and run:

1. Compile the program:

   ```bash
   gcc -o send_premade_dns send_premade_dns.c
   ```

2. Run the program (ensure `ip.bin` is present in the same directory):

   ```bash
   sudo ./send_premade_dns
   ```

### Generate DNS Query Packet

**Script**: `generate_dns_query.py`

This script generates a DNS query packet for a specific domain and saves it to a file.

#### How to run:

```bash
python3 generate_dns_query.py
```

### Generate DNS Reply Packet

**Script**: `generate_dns_reply.py`

This script generates a DNS reply packet for a specific domain, with spoofed answers and authority records, and saves it to a file.

#### How to run:

```bash
python3 generate_dns_reply.py
```

### DNS Spoofing with Authority

**Script**: `dns_spoof_authority.py`

This script listens for DNS queries for a specific domain and sends spoofed DNS replies with fake authority records.

#### How to run:

1. Edit the script to specify the target domain and spoofed IP addresses.
2. Run the script:

   ```bash
   sudo python3 dns_spoof_authority.py
   ```

### Basic DNS Spoofing

**Script**: `dns_spoof.py`

This script listens for DNS queries for a specific domain and sends spoofed DNS replies to redirect traffic.

#### How to run:

1. Edit the script to specify the domain to spoof and the IP address to redirect to.
2. Run the script:

   ```bash
   sudo python3 dns_spoof.py
   ```

### Notes

- Ensure you have the necessary permissions to run network manipulation scripts on your machine.
- Modify the IP addresses and domain names in the scripts as needed for your environment.
- These scripts are for educational and testing purposes in a controlled environment.
- Unauthorized use on networks you do not own or have permission to test is illegal and unethical.
