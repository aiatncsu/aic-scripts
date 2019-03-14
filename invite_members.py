from github import Github
import sys
# https://pygithub.readthedocs.io/en/latest/introduction.html

uname = sys.argv[1]
pw = sys.argv[2]
member_emails = ['jacklynchtds@gmail.com']

g = Github(uname, pw)

member_ids = []

for email in member_emails:
    query = email + ' in:email'
    unames = g.search_users(query)
    uname = ''
    if unames.totalCount == 0:
        continue
    else:
        uname = unames[0]

    member_ids.append(uname)

print(member_ids)
