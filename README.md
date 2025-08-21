# simple-port-scanner
A beginner-friendly Python script that scans a target system to check whether specific network ports are open or closed.
## Features
- Scans common ports like 22 (SSH), 80 (Web), 443 (HTTPS).
- Uses Python’s built-in socket library.
- Works on localhost or any chosen IP.

**⚠️ For educational purposes only.  
Do not scan systems without permission.**

PORTS#
Web → 80 & 443
Remote login → 22 (SSH), 3389 (RDP)
Email → 25, 110, 143
Files → 21, 69, 445
Databases → 3306, 1433, 27017
Networking basics → 53 (DNS), 67/68 (DHCP), 161 (SNMP)

// WHAT CAN BE PUT IN THE TERMINAL FOR THIS SCANNER
IP Address → direct, fast (e.g., 8.8.8.8)
Hostname/URL → user-friendly (e.g., scanme.nmap.org)
Subdomain → may point to different servers (mail.google.com, ftp.example.com)
Network ranges → scan multiple IPs at once (advanced)
