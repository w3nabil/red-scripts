# Lib 
import json
import os
import sys

# Logo with color to make it look more
logo = r""" _   _  ___  __  __ ____
| \ | |/ _ \|  \/  | __ )
|  \| | | | | |\/| |  _ \
| |\  | |_| | |  | | |_) |
|_| \_|\___/|_|  |_|____/ """

logo_with_color = f"""{"\033[1;33m"}{logo}{"\033[0m"}"""
# General Header
print(f"""{logo_with_color}      [Enjoy the NOMB Experience]""")
print("****************************************************************")
print("*             © Copyright NABIL, 2024                          *")
print("\n*           https://w3nabil.github.io/                         *")
print("****************************************************************")
print(f"{"\033[1;33m"}Caution: The NOMB Script was made for educational and ethical purposes. Misuse against any emails may have legal consequences.{"\033[0m"}")

print("Would you like to erase the existing config.json file? [Y/n][Default=Y]")
erase = input(" > ")
if erase.lower() in ['y', 'yes', '']: 
    try:
        os.remove("config.json")
        print("config.json erased")
    except FileNotFoundError:
        print("config.json not found")
elif erase.lower() in ['n', 'no']:
    print("Keeping existing config.json")
else:
    print(f"{"\033[31m"}Invalid Input{"\033[0m"}")
    sys.exit(1)

# Function to append json data
def add_config(sl, smtp_server, smtp_port, smtp_user, smtp_password):
    # Load existing data if config.json exists
    if os.path.exists("config.json"):
        with open("config.json", "r") as json_file:
            raw = json.load(json_file)
    else:
        raw = []  # Initialize as empty list if file doesn't exist

    # Prepare new data
    data = {
        'sl': int(sl),
        'smtp_server': smtp_server,
        'smtp_port': smtp_port,
        'smtp_user': smtp_user,
        'smtp_password': smtp_password
    }

    # Append new entry to the list
    raw.append(data)

    # Save updated data back to the file
    with open("config.json", "w") as json_file:
        json.dump(raw, json_file, indent=4)

# Asking for Number of mail account 
print("How many accounts would you like to add? [Default=1]")
sl = input(" > ") or 1

for i in range(int(sl)):
    # Asking for SMTP 
    print("Would you like to \n1) Use a gmail account for attack [Default][Recommended]\n2) or Your own SMTP Server")
    choosesmtp = input(" > ") or 1
    if int(choosesmtp) == 1:    
       smtp_server = 'smtp.gmail.com'
       smtp_port = 587
    elif int(choosesmtp) == 2:    
       print("Please enter SMTP Server Address (Example: smtp.yourserver.com)")
       smtp_server = input(" > ") or print("Can not attack withhblank smtp server address") & exit(1)
       print("Please enter SMTP Server Port Address [Default = 587]")
       smtp_port = int(input(" > ")) or 587
    print("Enter SMTP Username [For Gmail Users Please use your email address]")
    smtp_user = input(" > ")
    print("Enter SMTP Password [For Gmail and 2FA Users Please use App Password]")
    smtp_password = input(" > ")
    # Append data to config.json
    add_config(int(i) + 1, smtp_server, smtp_port, smtp_user, smtp_password)
    print("Updated config.json, Try running 'sudo nomb.py'\n\n")