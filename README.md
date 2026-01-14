# Cylock - Lightweight Cybersecurity Scanner 🛡️

**Cylock** is a modular, Python-based security auditing tool designed to detect common misconfigurations in web applications and network infrastructure.

> **Project Status:** Archived (v1.0 Capstone Prototype)

## 🚀 Key Features
* **Raw Socket Scanning:** Custom TCP handshake implementation (using `socket` library) to detect open ports without relying on Nmap.
* **Header Analysis:** Automated detection of missing security headers (`X-Frame-Options`, `Content-Security-Policy`) to prevent Clickjacking and XSS.
* **MITRE ATT&CK Mapping:** Automatically tags findings with relevant T-Codes (e.g., `T1046` for Network Service Discovery).

## 🛠️ Installation & Usage
```bash
# Clone the repository
git clone [https://github.com/Carrtik/Cylock.git](https://github.com/Carrtik/Cylock.git)

# Install dependencies
pip install -r requirements.txt

# Run the scanner
python main.py
