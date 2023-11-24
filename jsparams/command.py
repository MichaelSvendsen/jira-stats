from jsparams import args

class Command:
	"""Read the commmand runtime parameter"""

	def getCommand(self):
		if not self.commandRead:
			if self.args.command is not None:
				self.command = self.args.command

			self.commandRead = True

			if not self.validateCommand():
				raise Exception('Invalid command')

		return self.command

	def validateCommand(self):
		if self.command is None:
			return True

		return self.command.lower() in ['comment']

	def __init__(self):
		self.args = args
		self.commandRead = False
		self.command = None