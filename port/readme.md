# Port Scanner CLI

## 📌 Description
This is a simple automated port scanner written in Python. It allows you to scan a target host's ports within a specified range using multiple threads for efficiency.

## 🚀 Features
- Scan a specific **host**
- Multi-threading support for faster scanning
- Easy-to-use command-line arguments

## 📦 Installation
Make sure you have **Python 3.11.x** installed (built-in libraries like socket, sys, threading, agrparse are used). Then, download and use this script:

```bash
mkdir port-scanner
cd port-scanner
curl.exe -L -o basic.py https://raw.githubusercontent.com/w3nabil/red-scripts/main/port/basic.py
```

## 🛠 Usage
Run the script with the following command-line options:

```bash
python basic.py -H [host] -s [start port] -e [end port] -t [threads]
```

### 🎯 Example:
Scan **192.168.1.1** from **port 20** to **100**, using **500 threads**:
```bash
python basic.py -H 192.168.1.1 -s 20 -e 100 -t 500
```


### 📝 Command-Line Arguments:
| Flag | Full Option | Description | Required |
|------|------------|-------------|----------|
| `-H` | `--host`   | Target host to scan | ✅ Yes |
| `-s` | `--start`  | Start port number (default: 1) | ❌ No |
| `-e` | `--end`    | End port number (default: 10000)| ❌ No |
| `-t` | `--threads` | Number of threads (default: 1000) | ❌ No |

## 🆘 Help Menu
To view the help menu, run:
```bash
python basic.py --help
```

## 📜 License
This project is licensed under the [MIT](https://github.com/w3nabil/red-scripts/blob/main/LICENSE) License.



