# simple-port-scanner
A beginner-friendly Python script that scans a target system to check whether specific network ports are open or closed.
## Features
- Scans common ports like 22 (SSH), 80 (Web), 443 (HTTPS).
- Uses Python’s built-in socket library.
- Works on localhost or any chosen IP.
## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/simple-port-scanner.git
cd simple-port-scanner
## Example Output
Scanning 127.0.0.1...
Port 22 is OPEN
Port 80 is OPEN
Port 443 is CLOSED
## Disclaimer

⚠️ For educational purposes only.  
Do not scan systems without permission.

PORTS#
Web → 80 & 443
Remote login → 22 (SSH), 3389 (RDP)
Email → 25, 110, 143
Files → 21, 69, 445
Databases → 3306, 1433, 27017
Networking basics → 53 (DNS), 67/68 (DHCP), 161 (SNMP)
