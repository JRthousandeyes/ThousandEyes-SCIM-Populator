import os
import sys
import requests
import json
import csv
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


def add_user_scim(username, token, usernames, emails):
    url = f'https://{username}:{token}@api.thousandeyes.com/scim/v2'
    scim_data = {'name': f'{x}', 'email': f'{y}'}
    x = requests.post(url, data = scim_data)


if __name__ == '__main__':

    #email_input = pyip.inputEmail()
    username = "wsullivan+scim@thousandeyes.com"
    token = 'fzgiddp0rmyoozbwy2fxypdsk5t7fpei'

    global usernames
    global emails
    usernames = []
    emails = []

    csv_file_input = input("Please enter csv file: ")
    scan_csv(csv_file_input)
    print("List validation:")
    print(usernames)
    print(emails)
