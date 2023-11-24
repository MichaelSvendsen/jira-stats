from __future__ import annotations

import configparser

from jira import JIRA
from pathlib import Path

from jsparams.issues import Issues
from jsparams.command import Command


config = configparser.ConfigParser()
config.read(Path.home() / '.jira-stats' / 'jira-stats.ini')

server = config['production']['SERVER']
username = config['production']['USERNAME']
token = config['production']['TOKEN']

jira = JIRA(server=server, basic_auth=(username, token))

jsIssues = Issues()
issues = jsIssues.getIssues()

jsCommand = Command()
command = jsCommand.getCommand()


#print(str(args.issues))
#print(type(args.issues))

for x in issues:
	print(x)

print('command: ' + command)

#issue = jira.issue(args.issue)

#jira.add_comment(issue, args.comment)

#for issueval in args.issues:
#	print(issueval)
#	issue = jira.issue(issueval)
#	jira.add_comment(issue, args.comment)
