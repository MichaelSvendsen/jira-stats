from jsparams import args

class Fields:
	"""Read the fields that we operate on"""

	@property
	def fields(self):
		if not self.fieldsRead:
			if self.args.fields is not None:
				for strListOfFields in self.args.fields:
					for field in strListOfFields.split(','):
						self._fields.append(field.strip())

			self.fieldsRead = True
		
		return self._fields
	

	@fields.setter
	def fields(self, fs):
		self._fields = fs

	@property
	def fieldsRead(self):
		return self._fieldsRead

	@fieldsRead.setter
	def fieldsRead(self, fr):
		self._fieldsRead = fr
	
	@property
	def args(self):
		return self._args

	@args.setter
	def args(self, a):
		self._args = a
	

	def __init__(self, fs = [], fr = False, a = None):
		self.fields = fs
		self.fieldsRead = fr
		if a is None:
			self.args = args
		else:
			self.args = a