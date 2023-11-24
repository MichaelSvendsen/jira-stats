from jsparams import args

class Issues:
	"""Read issues from command line parameters"""

	def getIssues(self):
		if not self.issuesRead:
			if self.args.issue is not None:
				for issue in self.args.issue:
					self.issues.append(issue.strip())

			if self.args.issues is not None:
				for strListOfIssues in self.args.issues:
					for issue in strListOfIssues.split(','):
						self.issues.append(issue.strip())

			self.issuesRead = True

		return self.issues

	def __init__(self):
		self.issues = []
		self.issuesRead = False
		self.args = args

