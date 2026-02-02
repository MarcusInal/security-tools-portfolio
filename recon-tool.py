import argparse
import socket
import threading
import requests
import os 
import platform
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"  
)

open_ports = []
def scan_port(ip, port, Timeout=1):
    try: 
        sock = socket.socket()
        sock.settimeout(Timeout)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except Exception as e:
        pass

def run_portscanner(ip, start_port, end_port):
    global open_ports
    open_ports = []

    print(f"[+] Scannar {ip} från port {start_port} till {end_port}...\n")

    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if open_ports:
        print(f"[+] Öppna portar på {ip}:")
        for port in open_ports:
            print(f"  -  Port {port} är öppen")
    else:
        print(f"[-] Inga öppna portar hittades på {ip} i det angivna intervallet.")


def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} är uppe! (200 OK)")
        else:
            print(f"{url} är nere! Statuskod: {response.status_code}")
    except requests.RequestException as e:
        print(f"{url} är nere! Fel: {e}")

def run_webchecker(urls):
    print("[+] Startar webbplatskontroll...\n")
    threads = []
    for url in urls:
        t = threading.Thread(target=check_website, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Kontroll av webbplatser är klar.")

def ping_host(ip):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command =  f'ping {param} 1 -w 300 {ip} > nul 2>&1' if platform.system().lower()=='windows' else f'ping {param} 1 -W 1 {ip} > /dev/null 2>&1'

    response = os.system(command)

    return response == 0


def generate_ip_range(start_ip, end_ip):
    start_parts = list(map(int, start_ip.split('.')))
    end_parts = list(map(int, end_ip.split('.')))

    ip_range = []
    while start_parts <= end_parts:
        ip_range.append(".".join(map(str, start_parts)))
        start_parts[3] += 1
        if start_parts[3] > 255:
            start_parts[3] = 0
            start_parts[2] += 1
            if start_parts[2] > 255:
                start_parts[2] = 0
                start_parts[1] += 1
                if start_parts[1] > 255:
                    start_parts[1] = 0
                    start_parts[0] += 1

    return ip_range

def run_hostscanner(start_ip, end_ip):
    print(f"[+] Scannar IP-intervall från {start_ip} till {end_ip}...\n")
    logging.info(f"Startar hostscanner från {start_ip} till {end_ip}")

    ip_range = generate_ip_range(start_ip, end_ip)
    active_hosts = []
    threads = []

    def worker(ip):
        if ping_host(ip):
            print(f"[+] Host {ip} är aktiv")
            logging.info(f"Host {ip} är aktiv")
            active_hosts.append(ip)
        else:
            logging.debug(f"Host {ip} svarade inte på ping")


    for ip in ip_range:
        t = threading.Thread(target=worker, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Hostscanning är klar.")
    print(f"[+] Aktiva hosts hittade: {len(active_hosts)}" )
    for host in active_hosts:
        print(f"  -  {host}")



def main():
    parser = argparse.ArgumentParser(
        description="Recon scanner ( portscanner + webchecker)"
    ) 

    subparsers = parser.add_subparsers(dest="mode", help="Välj ett läge att köra verktyget i")

    # Portscanner subcommand
    portscanner_parser = subparsers.add_parser("portscan", help="Scanna portar på en Ip-adress" )
    portscanner_parser.add_argument("-ip", "--ipaddress", required=True, help="Mål IP-adress")
    portscanner_parser.add_argument("-s", type=int, default=1, help="Startport")
    portscanner_parser.add_argument("-e", type=int, default=1024, help="Slutport")

    # Webchecker subcommand
    web_parser = subparsers.add_parser("webcheck", help="Kolla status på en lista av webbplatser")
    web_parser.add_argument("-u", "--urls", nargs="+", required=True, help="Lista av URLs att kolla")

    hostscanner_parser = subparsers.add_parser("hostscan", help="Scanna ett IP-intervall för aktiva hosts")
    hostscanner_parser.add_argument("-s", "--start-ip", required=True, help="Start IP-adress")
    hostscanner_parser.add_argument("-e", "--end-ip", required=True, help="Slut IP-adress")
    
    args = parser.parse_args()

    if args.mode == "portscan":
        run_portscanner(args.ipaddress, args.s, args.e)
    elif args.mode == "webcheck":
        run_webchecker(args.urls)
    elif args.mode == "hostscan":
        run_hostscanner(args.start_ip, args.end_ip)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
