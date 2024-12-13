
![Logo](https://i.ibb.co.com/ChsyLnt/nomb.png)

# NOMB 
NOMB is a mass mail attack script that was developed to bypass the anti-spam filter for a specific timer. This script is originally made to develop better anti-spam filter system. 

*Caution: Using this scripts without the permission of the mail owner can be illegal. Avoid using mass mail accounts if you have low-end-pc*

## Download

Windows
```bash
mkdir nomb
cd nomb
curl.exe -L -o config.py https://raw.githubusercontent.com/w3nabil/red-scripts/main/nomb/config.py
curl.exe -L -o nomb.py https://raw.githubusercontent.com/w3nabil/red-scripts/main/nomb/nomb.py
```

Linux / Mac OS
```bash
mkdir nomb
cd nomb
curl -L -o config.py https://raw.githubusercontent.com/w3nabil/red-scripts/main/nomb/config.py
curl -L -o nomb.py https://raw.githubusercontent.com/w3nabil/red-scripts/main/nomb/nomb.py
```

## How to run the script 
Add single or multiple SMTP accounts using 
```bash
sudo python3 config.py
```

then run nomb 
```bash
sudo python3 nomb.py
```

## Customization 

If you want to run an attack with custom subjects and bodies, please list them at the following address. if there is no such file or file, you can create them manually.

```
nomb
└── src
    ├── mailbody.txt
    └── mailsubject.txt
```
Note: Currently this script supports only plain texts, html format is not allowed. 

Your `mailsubject.txt` or `mailbody.txt` should look like this: 
```
example subject 1
example subject 2
example subject 3 
``` 

Note: If you run the attack for n times, and you subjects less than n times then the script will automatically start selecting subjects from any lines of your subjects. This may not be the best thing to as this will be filtered by mail providers. [Read my observations to learn more why and how nomb works](./observation.md)

## Tested on:

| Mail Provider | Result | Last checked |
|---------------|--------|--------------|
| GMAIL | ✅ | *Thu Oct 24 2024 19:00:00 GMT+0000* |
| iCloud | ✅ | *Thu Oct 24 2024 19:00:00 GMT+0000* |
| ProtonMail | ✅ | *Thu Oct 24 2024 19:00:00 GMT+0000* |
| Yahoo | ❌ | *Thu Oct 24 2024 19:00:00 GMT+0000* |
| Outlook | ✅ | *Thu Oct 24 2024 19:00:00 GMT+0000* |

## Contributing

Contributions are welcome! 

To get started:
- Fork the repository
- Create a new branch for your feature or bug fix
- Submit a pull request

Feel free to reach out if you have any questions. Thank you for helping improve this project!
## License

[MIT](https://github.com/w3nabil/red-scripts/blob/1f4fad11baa297e56dd74f7dbb064de1d569a628/LICENSE)

