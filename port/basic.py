import socket
import threading
import sys
import argparse


def print_banner():
    logo = r"""
     ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
    |  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
    | |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
    |  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
    |_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
    """
    logo_with_color = f"""{"\033[1;33m"}{logo}{"\033[0m"}"""
    print(f"""{logo_with_color}      [Keep quiet and hack the world]""")
    print("\n****************************************************************")
    print("*             © Copyright NABIL, 2025                          *")
    print("\n*           https://w3nabil.github.io/                         *")
    print("****************************************************************")
    print(
        f"{"\033[1;33m"}Caution: The Port-SCANNER Script was made for educational and ethical purposes. Misuse against any system and/or server may have legal consequences.{"\033[0m"}"
    )


def is_target_online(target):
    try:
        socket.gethostbyname(target)
        return True
    except socket.gaierror:
        return False


def scan_port(target, port, open_ports):
    try:
        with socket.create_connection((target, port), timeout=1) as s:
            open_ports.append(port)
            print(f"\033[92m[+] Port {port} is open\033[0m")
    except (socket.timeout, ConnectionRefusedError):
        pass


def scan_target(target, start_port, end_port, threads):

    if not is_target_online(target):
        print("Target is offline.\n\nIf you are using any protocol before the hostname, please remove it and try again.\nFor example, use 'example.com' as a host instead of 'http://example.com'.")
        sys.exit(1)
    try:
        open_ports = []
        thread_list = []

        for port in range(start_port, end_port + 1): 
            thread = threading.Thread(target=scan_port, args=(target, port, open_ports))
            thread_list.append(thread)
            thread.start()

            if len(thread_list) >= threads:
                for t in thread_list:
                    t.join() 
                thread_list = []

        for t in thread_list:
            t.join()

        if open_ports:
            return open_ports
    except KeyboardInterrupt as e:
        print("Exiting...")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Port Scanner",
        usage="python basic.py -H [host](Required) -s [start port](Optional) -e [end port](Optional) -t [threads](Optional)",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("-H", "--host", required=True, help="Target host to scan [Required]")
    parser.add_argument(
        "-s", "--start", type=int, default=1, help="Start port number (default: 1)"
    )
    parser.add_argument(
        "-e", "--end", type=int, default=10000, help="End port number (default: 10000)"
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=1000,
        help="Number of threads (default: 1000)",
    )

    args = parser.parse_args()

    print_banner()
    print(f"\nScanning target: {args.host}\n")
    open_ports = scan_target(args.host, args.start, args.end, args.threads)

if __name__ == "__main__":
    main()
