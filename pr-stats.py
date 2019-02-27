#!/usr/bin/python

import sys
import requests
import getpass
# import json

if __name__ == "__main__":
    try:
        if str(sys.argv[1]) == "--help":
            print("------------THIS IS HELP PAGE------------.")
            print("To get statistics execute the program with keys:")
            print("./pr-stats.py <yours username> <username of repo owner>\
<repository>")
            print("------------------------------------------")
            exit()
        if str(sys.argv[1]) == "--version":
            print("pr-stats.py by Filip Chkhaidze, v0.1, EPAM Systems 2019")
            exit()
        if len(sys.argv) < 4:
            print("Not enough arguments. Please, see the help page with\
--help option")
            exit()
    except IndexError:
        print("No arguments. Please, see the help page with --help option")
        exit()

user = sys.argv[1]
repuser = sys.argv[2]
rep = sys.argv[3]
passwd = getpass.getpass(prompt='Enter your GIT password: ', stream=None)
url_api = "https://api.github.com/repos/%s/%s/pulls?page=1&per_page=100"
r = requests.get(url_api % (repuser, rep), auth=(user, passwd)).json()
# r_sorted = json.dumps(r, indent=4)

try:
    for i in range(100):
        print("Title: %s" % r[i]['title'])
        print("Owner: %s" % r[i]['head']['repo']['owner']['login'])
        print("State: %s" % r[i]['state'])
        print("Merged_at: %s" % r[i]['merged_at'])
        print("Created_at: %s" % r[i]['head']['repo']['created_at'])
        print("Pushed_at: %s" % r[i]['head']['repo']['pushed_at'])
        print("Updated_at: %s" % r[i]['head']['repo']['updated_at'])
        print("Closed_at: %s" % r[i]['closed_at'])
        print("Watchers: %s" % r[i]['head']['repo']['watchers'])
        print("Size: %s" % r[i]['head']['repo']['size'])
        print("-----------------------------------------------")
except IndexError:
    pass
except UnicodeEncodeError:
    pass
