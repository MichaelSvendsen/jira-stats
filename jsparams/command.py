from jsparams import args

class Command:
	"""Read the commmand runtime parameter"""

	def _validateCommand(self):
		if self.command is None:
			return True

		return self.command.lower() in ['comment', 'info']

	@property
	def command(self):
		if not self.commandRead:
			if self.args.command is not None:
				self._command = self.args.command

			self.commandRead = True

			if not self._validateCommand():
				raise Exception('Invalid command')

		return self._command

	@command.setter
	def command(self, c):
		self._command = c

	@property
	def commandRead(self):
		return self._commandRead

	@commandRead.setter
	def commandRead(self, cr):
		self._commandRead = cr
	
	@property
	def args(self):
		return self._args

	@args.setter
	def args(self, a):
		self._args = a
	

	def __init__(self):
		self.args = args
		self.commandRead = False
		self.command = None