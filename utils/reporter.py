import sys
import json
import time
from colorama import Fore, Style, init

# Initialize colorama for Windows/Linux compatibility
init(autoreset=True)

def print_banner():
    banner = f"""
    {Fore.CYAN}
      ______   __     __   __       ______    ______   __  __
     /      \ /  \   /  | /  |     /      \  /      \ /  |/  |
    /$$$$$$  |$$  \ /$$/  $$ |    /$$$$$$  |/$$$$$$  |$$ |$$ |
    $$ |  $$/  $$  /$$/   $$ |    $$ |  $$ |$$ |  $$/ $$ |$$ |
    $$ |        $$ $$/    $$ |    $$ |  $$ |$$ |      $$ |$$ |
    $$ |   __    $$$/     $$ |    $$ |  $$ |$$ |   __ $$ |$$ |
    $$ \__/  |    $$ |    $$ |____$$ \__$$ |$$ \__/  |$$ |$$ |__
    $$    $$/     $$ |    $$      $$    $$/ $$    $$/ $$ |$$    |
     $$$$$$/      $$/     $$$$$$$$/$$$$$$/   $$$$$$/  $$/ $$$$$$/
    {Style.RESET_ALL}
    {Fore.YELLOW}[*] Cylock v1.0 - Capstone Security Scanner{Style.RESET_ALL}
    """
    print(banner)

def print_info(message):
    print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} {message}")

def print_success(message):
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {message}")

def print_warning(message, mitre_id=None):
    if mitre_id:
        print(f"{Fore.RED}[VULN]{Style.RESET_ALL} {message} {Fore.MAGENTA}(MITRE: {mitre_id}){Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}")

def print_error(message):
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")

def save_report_json(target, open_ports, missing_headers):
    report = {
        "target": target,
        "timestamp": time.ctime(),
        "vulnerabilities": []
    }

    for port in open_ports:
        report["vulnerabilities"].append({
            "type": "Open Port",
            "detail": f"Port {port} Open",
            "mitre_id": "T1046",
            "severity": "Medium"
        })

    for header in missing_headers:
        report["vulnerabilities"].append({
            "type": "Missing Header",
            "detail": f"Missing {header}",
            "mitre_id": "T1190",
            "severity": "Low"
        })

    filename = f"scan_report_{target}.json"
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print_success(f"Report saved to {filename}")
