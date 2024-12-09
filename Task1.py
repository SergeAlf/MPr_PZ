# Easy - Простий сканер портів на основі socket

import socket

def simple_port_scanner(target_ip, start_port, end_port):
    print(f"Scanning ports on {target_ip} from {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.settimeout(1)
                s.connect((target_ip, port))
                print(f"Port {port} is open")
            except (socket.timeout, ConnectionRefusedError):
                pass

if __name__ == "__main__":
    target_ip = "scanme.nmap.org"
    simple_port_scanner(target_ip, 1, 1024)