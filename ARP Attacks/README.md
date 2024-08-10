# Man-in-the-Middle and ARP Poisoning Scripts

## Overview

This section contains scripts designed to demonstrate Man-in-the-Middle (MITM) attacks and ARP poisoning techniques. These scripts are intended for educational purposes and illustrate how network communications can be intercepted and manipulated.

### Scripts

1. **mitm_tcp.py**: Performs a TCP-based MITM attack by intercepting and modifying packets between two hosts.
2. **arp_poisoning_mitm.py**: Executes an ARP poisoning attack to redirect traffic between two hosts through the attacker's machine.
3. **arp_request.py**: Sends a spoofed ARP request to associate an attacker's MAC address with a spoofed IP address.

## Requirements

- Python 3.x
- Scapy library
- Root or sudo privileges to execute network manipulation scripts.

To install Scapy, run:
```bash
pip install scapy
```

## Usage

### TCP Man-in-the-Middle Attack

**Script**: `mitm_tcp.py`

This script intercepts TCP packets between two hosts and modifies the payload to replace occurrences of a specified string.

#### How to run:

1. Edit the script to specify the IP and MAC addresses of the target hosts (IP_A, MAC_A, IP_B, MAC_B) and the attacker's machine (IP_M, MAC_M).
2. Specify the string (`FIRST_NAME`) to be replaced in the TCP payload.
3. Run the script:

```bash
python3 mitm_tcp.py
```

### ARP Poisoning Man-in-the-Middle Attack

**Script**: `arp_poisoning_mitm.py`

This script sends spoofed ARP requests to two target hosts to associate the attacker's MAC address with the IP addresses of each host, allowing interception of their communications.

#### How to run:

1. Edit the script to specify the IP and MAC addresses of the target hosts (IP_A, MAC_A, IP_B, MAC_B) and the attacker's machine (IP_M, MAC_M).
2. Run the script:

```bash
python3 arp_poisoning_mitm.py
```

### Spoofed ARP Request

**Script**: `arp_request.py`

This script sends a spoofed ARP request to a target host, associating a spoofed IP address with the attacker's MAC address.

#### How to run:

1. Edit the script to specify the target IP and MAC address (IP_target, MAC_target) and the spoofed IP and MAC address (IP_spoofed, MAC_spoofed).
2. Run the script:

```bash
python3 arp_request.py
```

### Notes

- Ensure you have the necessary permissions to run network manipulation scripts on your machine.
- These scripts are for educational and testing purposes in a controlled environment.
- Unauthorized use on networks you do not own or have permission to test is illegal and unethical.
