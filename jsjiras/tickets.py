class Tickets:
	"""Aggregate values on lists of jira tickets/issues"""

	def __init__(self, issues):
		self._issues = issues

	@property
	def issues(self):
		return self._issues
	