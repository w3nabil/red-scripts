# XST, Host Header Injection, and Clickjacking Scanner

This script is designed to test a target server for vulnerabilities related to **Cross-Site Tracing (XST)**, **Host Header Injection**, and **Clickjacking**. It sends custom HTTP requests to the target server, checks for specific vulnerabilities, and saves the raw responses to a uniquely named text file.

### Features

- **Cross-Site Tracing (XST)**: Detects if the server is vulnerable to Cross-Site Tracing by sending a `TRACE` request with a malicious user-agent.
- **Host Header Injection**: Checks for Host Header Injection vulnerabilities by sending a `GET` request with a custom `Host` header.
- **Clickjacking**: Tests for Cross-Frame Scripting and Clickjacking by sending a standard `GET` request and checking for the absence of `X-Frame-Options` headers.

### File Naming

The raw response from each test is saved in a `.txt` file named after the target IP address. The dots (`.`) in the IP address are replaced with underscores (`_`). If the file already exists, a number is appended to create a unique filename.

For example:
- `103.10.12.10` becomes `103_10_12_10.txt`
- If `103_10_12_10.txt` exists, the next file will be named `103_10_12_10_1.txt`, and so on.

### Requirements

- Python 3.x
- No additional libraries required (built-in libraries like `socket`, `sys`, `http.client` are used).

### Usage

1. Clone this repository or download the script.
2. Run the script from the command line:

```bash
python xst.py <target_ip> <port>
```

Replace `<target_ip>` with the IP address of the target server and `<port>` with the port number (e.g., 80 for HTTP, 443 for HTTPS).

### Example

```bash
python xst.py 103.10.12.10 80
```

### Output

- The script will display results on the terminal, indicating whether the server is vulnerable to **XST**, **Host Header Injection**, or **Clickjacking**.
- Raw HTTP responses from each test are saved in a file named after the target IP address (e.g., `103_10_12_10.txt`).

### License

This script is made for educational and ethical purposes. Misuse against any system and/or server may have legal consequences.

**© Copyright NABIL, 2025**
