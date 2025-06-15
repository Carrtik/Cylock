import requests
from utils.reporter import print_info, print_warning, print_success, print_error

SECURITY_HEADERS = ['X-Frame-Options', 'X-Content-Type-Options', 'Content-Security-Policy']

def scan_headers(url):
    print_info(f"Checking HTTP Headers on {url}...")
    missing_list = []

    try:
        if not url.startswith("http"):
            url = "http://" + url

        response = requests.get(url, timeout=3)

        for check in SECURITY_HEADERS:
            if check not in response.headers:
                print_warning(f"Missing Header: {check}", mitre_id="T1190")
                missing_list.append(check)

        if not missing_list:
            print_success("All key security headers present.")

    except Exception as e:
        print_error(f"Connection failed: {str(e)}")

    return missing_list
