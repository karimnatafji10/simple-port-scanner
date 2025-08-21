# range_port_scanner.py
import socket
import argparse

def scan_port(target, port, timeout=0.5):
    """Return True if port is open on target."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((target, port)) == 0

def main():
    parser = argparse.ArgumentParser(description="Simple range-based TCP port scanner")
    parser.add_argument("target", help="IP or hostname (e.g., 127.0.0.1 or scanme.nmap.org)")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1000, help="End port (default: 1000)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Socket timeout seconds (default: 0.5)")
    parser.add_argument("--show-closed", action="store_true", help="Also print closed ports")
    args = parser.parse_args()

    # Resolve hostname once (helps with speed & clarity)
    try:
        resolved_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"Could not resolve target: {args.target}")
        return

    print(f"Scanning {args.target} ({resolved_ip}) ports {args.start}-{args.end}...\n")

    open_ports = []
    for port in range(args.start, args.end + 1):
        is_open = scan_port(resolved_ip, port, args.timeout)
        if is_open:
            print(f"[OPEN ] {port}")
            open_ports.append(port)
        elif args.show_closed:
            print(f"[CLOSED] {port}")

    print("\nScan complete.")
    if open_ports:
        print("Open ports:", ", ".join(map(str, open_ports)))
    else:
        print("No open ports found in this range.")

if __name__ == "__main__":
    main()
