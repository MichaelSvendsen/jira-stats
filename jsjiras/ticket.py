class Ticket:
	"""Standardisation of access to jira tickets/issues"""
	
	def __init__(self, issue):
		self._issue = issue

	@property
	def issue(self):
		return self._issue
	
	@property
	def issuetype(self):
		return self.issue.fields.issuetype.name
	
	@property
	def key(self):
		return self.issue.key

	@property
	def status(self):
		return self.issue.fields.status.name

	@property
	def summary(self):
		return self.issue.fields.summary

	@property
	def description(self):
		return self.issue.fields.description
	
	@property
	def watchers(self):
		self.issue.fields.watches.find(self.issue.key)
		return [w.displayName for w in self.issue.fields.watches.watchers]

	@property
	def watchCount(self):
		return self.issue.fields.watches.watchCount
	
	
	
