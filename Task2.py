# Hard - Сканер портів з використанням Scapy та SYN флагів

from scapy.all import IP, TCP, sr1

def advanced_syn_scanner(target_ip, ports):
    print(f"Scanning ports on {target_ip} with SYN flags...")
    for port in ports:
        packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        if response:
            if response[TCP].flags == "SA":  # SYN + ACK
                print(f"Port {port} is open.")
            elif response[TCP].flags == "RA":  # RST + ACK
                print(f"Port {port} is closed.")

if __name__ == "__main__":
    target_ip = "scanme.nmap.org"
    ports = [22, 80, 443]
    advanced_syn_scanner(target_ip, ports)