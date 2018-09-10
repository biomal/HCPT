class AttributeMissingException(Exception):
	def __init__(self,attribute):
		print 'Error: Value not specified for Attribute:' + attribute.name