# TUN/TAP Interface Scripts

## Overview

This section contains scripts for creating and managing TUN interfaces, demonstrating how to handle packet routing and spoofing using these virtual network interfaces. TUN interfaces operate at the network layer, handling IP packets, and are useful for creating VPNs and testing network traffic handling.

### Scripts

1. **tun_client.py**: Implements a TUN client that sends and receives packets through a TUN interface.
2. **tun_server.py**: Implements a TUN server that handles packets sent to a TUN interface.
3. **tun-all.py**: A script that sets up a TUN interface and processes ICMP packets, spoofing responses.
4. **tun.py**: A simple script to create a TUN interface and handle basic packet processing.

## Requirements

- Python 3.x
- Scapy library
- Root or sudo privileges to create TUN/TAP interfaces.

To install Scapy, run:
```bash
pip install scapy
```

## Usage

### TUN Client

**Script**: `tun_client.py`

This script sets up a TUN interface, binds a UDP socket, and exchanges packets with the TUN interface.

#### How to run:

```bash
python3 tun_client.py
```

### TUN Server

**Script**: `tun_server.py`

This script sets up a TUN interface on the server side to handle packets received from a client.

#### How to run:

```bash
python3 tun_server.py
```

### TUN All

**Script**: `tun-all.py`

This script creates a TUN interface, processes ICMP packets, and sends spoofed ICMP responses.

#### How to run:

```bash
python3 tun-all.py
```

### Basic TUN Setup

**Script**: `tun.py`

This script creates a TUN interface and sets it up with a static IP address.

#### How to run:

```bash
python3 tun.py
```

### Notes

- Ensure you have the necessary permissions to create and manage TUN/TAP interfaces on your system.
- Modify IP addresses and network configurations in the scripts as needed for your environment.
- Use these scripts only in controlled environments with explicit permission, as unauthorized use is illegal and unethical.
