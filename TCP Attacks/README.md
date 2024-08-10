# Network Attack Simulation Scripts

## Overview

This section contains scripts designed to simulate various network attacks, including session hijacking, TCP reset attacks, and SYN flooding. These scripts are intended for educational purposes and demonstrate how network protocols can be manipulated for attack vectors.

### Scripts

1. **sessionhijack.py**: Performs a session hijacking attack by spoofing TCP packets to inject data into an existing TCP session.
2. **reset.py**: Executes a TCP reset attack by sending forged TCP reset packets to terminate a TCP connection.
3. **synflood.py**: Launches a SYN flood attack using Python to overwhelm a target with TCP SYN packets.
4. **synflood.c**: A C program that performs a SYN flood attack on a specified target using raw sockets.

## Requirements

- Python 3.x
- Scapy library (for Python scripts)
- GCC compiler (for compiling the C program)
- Root or sudo privileges to execute scripts that require raw socket operations.

To install Scapy, run:
```bash
pip install scapy
```

To compile the C program, use:
```bash
gcc -o synflood synflood.c
```

## Usage

### Session Hijacking

**Script**: `sessionhijack.py`

This script performs a session hijacking attack by capturing packets in a TCP session and injecting commands or data.

#### How to run:

```bash
python3 sessionhijack.py <client_ip> <server_ip>
```

### TCP Reset Attack

**Script**: `reset.py`

This script sends forged TCP reset packets to terminate a TCP connection between a client and a server.

#### How to run:

```bash
python3 reset.py <client_ip> <server_ip>
```

### SYN Flood Attack (Python)

**Script**: `synflood.py`

This script generates a flood of TCP SYN packets to a target IP address, attempting to overwhelm the target's resources.

#### How to run:

```bash
python3 synflood.py
```

### SYN Flood Attack (C)

**Program**: `synflood.c`

This C program sends a continuous stream of TCP SYN packets to a target, exploiting raw sockets to achieve high packet throughput.

#### How to compile and run:

```bash
gcc -o synflood synflood.c
./synflood <target_ip> <target_port>
```

### Notes

- Ensure you have the necessary permissions to run network manipulation scripts on your machine.
- These scripts are for educational and testing purposes in a controlled environment.
- Unauthorized use on networks you do not own or have permission to test is illegal and unethical.
