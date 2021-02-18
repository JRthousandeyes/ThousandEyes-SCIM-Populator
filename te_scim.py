import os
import sys
import requests
import json
import csv
import re
#import pyinputplus as pyip

'''
ThosuandEyes SCIM user populator
Year: 2021
Contact: Collin Sullivan (wsullivan@thusandeyes.com, collsull@cisco.com)

Parses CSV file following standard formatting rules and scrapes users and emails to add
as users to specific organization.

'''


def scan_csv(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\nCSV column name verification: {", ".join(row)}\n')
                line_count += 1
            else:
                print(f'Username: {row[0]} Email: {row[1]}')
                usernames.append(row[0])
                emails.append(row[1])
                line_count += 1
        print("\n")


def validate_emails():
    email_format_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    for email_address in emails:
        if(re.search(email_format_regex, email_address)):
            print(f"SCIM Email validated: {email_address}")
        else:
            print(f"SCIM Email not in proper format: {email_address}")
    print("\n")


def add_user_scim(usernames, emails):
    url = f'https://{username}:{token}@api.thousandeyes.com/scim/v2'
    for x, y in zip(usernames, emails):
        scim_data = {'name': f'{x}', 'email': f'{y}'}
        post_request = requests.post(url, data = scim_data)
        print(f"Added user {x} with email {y} to ThousaandEyes platform.")
        print(post_request)


if __name__ == '__main__':

    username = "enter your admin TE email here"
    token = 'enter your token here'

    global usernames
    global emails
    usernames = []
    emails = []

    csv_file_input = input("Please enter csv file: ")
    scan_csv(csv_file_input)
    print("Email validation:")
    validate_emails()
    add_user_scim(usernames, emails)
