import socket
from utils.reporter import print_info, print_warning, print_success

def scan_ports(target_ip, ports):
    print_info(f"Starting Socket Scan on {target_ip}...")
    open_ports = []

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))

            if result == 0:
                print_warning(f"Port {port} is OPEN", mitre_id="T1046")
                open_ports.append(port)
            s.close()
        except:
            pass

    if not open_ports:
        print_success("No open ports found in standard list.")
    return open_ports
