from __future__ import annotations

from jira import JIRA

from jsparams.issues import Issues
from jsparams.command import Command
from jsparams.fields import Fields

from jsconfig.configuration import Configuration


conf = Configuration('production')

jira = JIRA(server=conf.server, basic_auth=(conf.username, conf.token))

jsIssues = Issues()

jsCommand = Command()

jsFields = Fields()


#print(str(args.issues))
#print(type(args.issues))

for x in jsIssues.issues:
	print(x)

print('command: ' + jsCommand.command)

if jsCommand.command == 'info':
	for issueId in jsIssues.issues:
		issue = jira.issue(issueId)
		print('Issue: ' + str(issue.key))
		for f in jsFields.fields:
			if f == 'status':
				print('\t' + f + ': ' + issue.fields.status.name)
			if f == 'issuetype':
				print('\t' + f + ': ' + issue.fields.issuetype.name)
			if f == 'summary':
				print('\t' + f + ': ' + issue.fields.summary)

#issue = jira.issue(args.issue)

#jira.add_comment(issue, args.comment)

#for issueval in args.issues:
#	print(issueval)
#	issue = jira.issue(issueval)
#	jira.add_comment(issue, args.comment)
