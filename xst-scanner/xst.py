import socket
import sys
import os

def print_banner():
    logo = r"""
    __  ______ _____   ____ 
    \ \/ / ___|_   _| / ___|  ___ __ _ _ __  _ __   ___ _ __ 
     \  /\___ \ | |   \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| 
     /  \ ___) || |    ___) | (_| (_| | | | | | | |  __/ | 
    /_/\_\____/ |_|   |____/ \___\__,_|_| |_|_| |_|\___|_|"""
    logo_with_color = f"""{"\033[1;33m"}{logo}{"\033[0m"}"""
    print(f"""{logo_with_color}      [Enjoy the SCANNING XST Experience]""")
    print("****************************************************************")
    print("*             © Copyright NABIL, 2025                          *")
    print("\n*           https://w3nabil.github.io/                         *")
    print("****************************************************************")
    print(
        f"{"\033[1;33m"}Caution: The XST-SCANNER Script was made for educational and ethical purposes. Misuse against any system and/or server may have legal consequences.{"\033[0m"}"
    )

def test_xst(target, port):
    try:
        buffer1 = "TRACE / HTTP/1.1\r\n"
        buffer2 = "User-agent: <script>alert(1);</script>\r\n"
        buffer3 = f"Host: {target}\r\n\r\n"
        data = ""

        with socket.create_connection((target, port), timeout=10) as s:
            s.sendall((buffer1 + buffer2 + buffer3).encode())
            data = s.recv(4096).decode()

        if "<script>alert(1);</script>" in data.lower():
            xst_result = " Yes "
        else:
            xst_result = " No  "

        return data, xst_result
    except Exception as e:
        xst_result = "Error"
        return "", xst_result


def test_host_header_injection(target, port):
    try:

        buffer1 = "GET / HTTP/1.1\r\n"
        buffer2 = "Host: https://logger-i0r8.onrender.com\r\n\r\n"
        data = ""

        with socket.create_connection((target, port), timeout=5) as s:
            s.sendall((buffer1 + buffer2).encode())
            data = s.recv(4096).decode()

        if "logger-i0r8.onrender.com" in data.lower():
            header_result = " Yes "
        else:
            header_result = " No "

        return data, header_result
    except Exception as e:
        header_result = "Error"
        return "", header_result

def test_clickjacking(target, port):
    try:

        buffer = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"
        data = ""

        with socket.create_connection((target, port), timeout=5) as s:
            s.sendall(buffer.encode())
            data = s.recv(4096).decode()

        if "x-frame-options" in data.lower():
            click_result = " No "
        else:
            click_result = " Yes "

        return data, click_result
    except Exception as e:
        click_result = "Error"
        return "", click_result

def main(argv):
    if len(argv) < 3:
        print_banner()
        print(f"{"\033[94m"}Usage: {argv[0]} <host> <port>{"\033[0m"}")
        sys.exit(1)

    target = argv[1]
    port = int(argv[2])

    print_banner()

    xst_data, xst_result = test_xst(target, port)
    host_data, header_result = test_host_header_injection(target, port)
    clickjacking_data, click_result = test_clickjacking(target, port)

    print(f"\n\n\t\t{"\033[1;33m"}Target: {target}:{port}{"\033[0m"}")
    print(f"\n\t{"\033[32m"}SL  | \tAttack Type           | \tVulnerable? {"\033[0m"}")
    print(f"\t---------------------------------------------------------------{"\033[0m"}")
    print(f"\t1   | \tCross Site Tracing    | \t{xst_result}     ")
    print(f"\t2   | \tHost Header Injection | \t{header_result}      ")
    print(f"\t3   | \tClickjacking          | \t{click_result}     ")
    print(f"\t---------------------------------------------------------------{"\033[0m"}")
    print("")

    base_filename = target.replace(".", "_") + "_" + str(port)

    if not os.path.exists("./log"):
        os.makedirs("./log")

    for i in range(1, 999):
        filename = f"./log/{base_filename}_{i}.txt"
        try:
         with open(filename, "x") as f: 
                f.write("===== Raw Headers from XST Test ====\n")
                f.write(xst_data + "\n\n\n")
                f.write("\n===== Raw Headers from Host Header Injection Test =====\n")
                f.write(host_data + "\n\n\n")
                f.write("\n===== Raw Headers from Clickjacking Test =====\n")
                f.write(clickjacking_data + "\n\n\n")
                print(f"Raw Headers Reponses were saved as {filename}")
                break
        except FileExistsError:
            continue

if __name__ == "__main__":
    main(sys.argv)
