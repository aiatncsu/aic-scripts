from github import Github, GithubException
import sys
import pandas as pd
import time
# https://pygithub.readthedocs.io/en/latest/introduction.html

uname = sys.argv[1]
pw = sys.argv[2]

csv_path = 'members.csv'
membership = pd.read_csv(csv_path)
member_emails = membership.iloc[:,0].values.tolist()

g = Github(uname, pw)
aic = Github.get_organization(g, 'aiatncsu')

members = []

for email in member_emails:
    query = email + ' in:email'
    unames = g.search_users(query)
    uname = ''
    try:
        if unames.totalCount == 0:
            continue
        else:
            uname = unames[0]
    except GithubException as e:
        if e[0] == 403:  # sent too many requests in the time limit
            sys.exit()

    members.append(uname)

print(members)

for member in members:
    try:
        aic.invite_user(member)
    except GithubException as e:
        # verbose way of checking the proper exception
        if e[1]['errors'][0]['message'] == 'Invitee is already a part of this org':
            continue
        # less-verbose way (check the error code)
        if e[0] == 403:  # sent too many requests in the time limit
            sys.exit()
