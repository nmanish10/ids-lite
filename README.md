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
- Scapy  
- Npcap (for Windows)

### Install Dependencies

```bash
pip install scapy
```

## ▶️ How to Run

On Windows:
```bash
python ids_lite.py
```
*Run Command Prompt as Administrator.*

On Linux:
```bash
sudo python3 ids_lite.py
```

## 🧪 Testing

Use `nmap` to simulate a port scan:

```bash
nmap -p 1-100 <your-local-IP>
```

Replace `<your-local-IP>` with your actual local IP address.

## 📁 Files

- `ids_lite.py` – Main IDS script  
- `README.md` – Project instructions  

## 🧑‍💻 Author

**Manish N** – Built as part of a cybersecurity assignment for alternate assessment.