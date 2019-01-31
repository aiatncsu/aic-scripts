import pandas as pd
import sys

"""
Handles a TypeForm CSV with
- email as second column 
- multiple-choice answers as unlabeled columns
Exports a CSV of all user emails who have the specified interet (tag)
"""

tag = sys.argv[1]
csv_path = "users.csv"

users = pd.read_csv(csv_path)

has_tag = users.apply(lambda r: r.str.contains(tag, case=False).any(), axis=1)

users = users[has_tag]

user_emails = users.iloc[:,1]

user_emails.to_csv("user_emails.csv")
