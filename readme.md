# IDS Lite 🛡️

A lightweight Intrusion Detection System written in Python using Scapy.  
It detects potential port scans based on unusual activity in a short time window.

## 🔧 Features

- Real-time TCP packet sniffing
- Port scan detection
- Alerts for suspicious IPs
- Lightweight and terminal-based

## 📦 Requirements

- Python 3.x
- scapy
- npcap (Windows)

Install dependencies:

```bash
pip install scapy
▶️ How to Run
bash
Copy
Edit
python ids_lite.py
On Windows, run Command Prompt as Administrator.
On Linux, use sudo python3 ids_lite.py.

🧪 Testing
Use nmap to simulate port scans:

bash
Copy
Edit
nmap -p 1-100 <your-local-IP>
📁 Files
ids_lite.py – Main IDS script

README.md – Project instructions

🧑‍💻 Author
Manish N – Built as part of a cybersecurity assignment for alternate assessment.