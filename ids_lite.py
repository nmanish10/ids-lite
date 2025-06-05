from scapy.all import sniff, IP, TCP
from collections import defaultdict
from datetime import datetime, timedelta

# Track connections per IP
connection_tracker = defaultdict(list)
PORT_SCAN_THRESHOLD = 20
TIME_WINDOW = 10  # seconds

def detect_port_scan(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_src = packet[IP].src
        dport = packet[TCP].dport

        # Record the time of the attempt
        now = datetime.now()
        connection_tracker[ip_src].append((dport, now))

        # Clean up old entries
        connection_tracker[ip_src] = [
            (port, timestamp) for port, timestamp in connection_tracker[ip_src]
            if now - timestamp < timedelta(seconds=TIME_WINDOW)
        ]

        # Detect port scan
        unique_ports = set(port for port, _ in connection_tracker[ip_src])
        if len(unique_ports) > PORT_SCAN_THRESHOLD:
            print(f"[ALERT] Possible port scan detected from {ip_src}")
            connection_tracker[ip_src] = []  # Reset after alert

print("🔍 IDS Lite is running. Press Ctrl+C to stop.")
sniff(filter="tcp", prn=detect_port_scan, store=0)
