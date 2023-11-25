from jsconfig import config

class Configuration:
	"""Read local configuration file"""

	def getConfiguration(self):
		conf = {}

		conf['server'] = self.server()
		conf['username'] = self.username()
		conf['token'] = self.token()

		return conf

	@property
	def server(self):
		return self._server
	
	@server.setter
	def server(self, s):
		self._server = s

	@property
	def username(self):
		return self._username

	@username.setter
	def username(self, un):
		self._username = un

	@property
	def token(self):
		return self._token

	@token.setter
	def token(self, t):
		self._token = t


	def __init__(self, env):
		self.env = env

		self._server = config[env.lower()]['SERVER']
		self._username = config[env.lower()]['USERNAME']
		self._token = config[env.lower()]['TOKEN']	