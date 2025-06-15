import argparse
import socket
import sys
from modules.port_scanner import scan_ports
from modules.header_scanner import scan_headers
from utils.reporter import print_banner, print_info, print_error, save_report_json

TARGET_PORTS = [21, 22, 80, 443, 3306, 8080]

def main():
    print_banner()
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="Target IP or Hostname")
    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print_error("Could not resolve hostname.")
        sys.exit(1)

    print_info(f"Target: {args.target} ({target_ip})")

    # Run Scans and Capture Data
    open_ports = scan_ports(target_ip, TARGET_PORTS)
    missing_headers = scan_headers(args.target)

    # Save Report
    save_report_json(args.target, open_ports, missing_headers)

if __name__ == "__main__":
    main()
