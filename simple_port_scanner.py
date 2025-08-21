import socket

# Target IP address (example: google.com)
target = ""   

# Range of ports to scan
ports = [21, 22, 80, 443, 3306]

print(f"Scanning {target}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    
    sock.close()

