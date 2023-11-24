from __future__ import annotations

import re
import configparser
import argparse

from jira import JIRA
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path.home() / '.jira-stats' / 'jira-stats.ini')

server = config['production']['SERVER']
username = config['production']['USERNAME']
token = config['production']['TOKEN']


jira = JIRA(server=server, basic_auth=(username, token))

parser = argparse.ArgumentParser()

parser.add_argument("--action", help="The command we wish to perform")
parser.add_argument("--issue", help="The issue number we operate on", action="append")
parser.add_argument("--issues", help="The issue numbers we operate on", action="append")
parser.add_argument("--comment", help="If we can add a comment this is the text for it")

args = parser.parse_args()

issues = []

if args.issue is not None:
	for issue in args.issue:
		issues.append(issue.strip())

if args.issues is not None:
	for strListOfIssues in args.issues:
		for issue in strListOfIssues.split(','):
			issues.append(issue.strip())


#print(str(args.issues))
#print(type(args.issues))

for x in issues:
	print(str(x))
	print(type(x))

#issue = jira.issue(args.issue)

#jira.add_comment(issue, args.comment)

#for issueval in args.issues:
#	print(issueval)
#	issue = jira.issue(issueval)
#	jira.add_comment(issue, args.comment)
