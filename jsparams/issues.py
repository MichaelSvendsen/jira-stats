from jsparams import args

class Issues:
	"""Read issues from command line parameters"""

	@property
	def issues(self):
		if not self.issuesRead:
			if self.args.issue is not None:
				for issue in self.args.issue:
					self._issues.append(issue.strip())

			if self.args.issues is not None:
				for strListOfIssues in self.args.issues:
					for issue in strListOfIssues.split(','):
						self._issues.append(issue.strip())

			self.issuesRead = True

		return self._issues

	@issues.setter
	def issues(self, iss):
		self._issues = iss

	@property
	def issuesRead(self):
		return self._issuesRead

	@issuesRead.setter
	def issuesRead(self, ir):
		self._issuesRead = ir

	@property
	def args(self):
		return self._args

	@args.setter
	def args(self, a):
		self._args = a


	def __init__(self, iss = [], ir = False, a = None):
		self.issues = iss
		self.issuesRead = ir
		if a is None:
			self.args = args
		else:
			self.args = a

