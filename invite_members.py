from github import Github
from github import GithubException
import sys
# https://pygithub.readthedocs.io/en/latest/introduction.html

uname = sys.argv[1]
pw = sys.argv[2]
member_emails = ['jacklynchtds@gmail.com']

g = Github(uname, pw)
aic = Github.get_organization(g, 'aiatncsu')

print("getting members")
#print(aic)
#print(aic.get_members()[1])

members = []

for email in member_emails:
    query = email + ' in:email'
    unames = g.search_users(query)
    uname = ''
    if unames.totalCount == 0:
        continue
    else:
        uname = unames[0]

    members.append(uname)

#print(members)

for member in members:
    try:
        aic.invite_user(member)
    except GithubException as e:
        if e[1]['errors'][0]['message'] == 'Invitee is already a part of this org':
            continue
