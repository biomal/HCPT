class AttributeDependancyException(Exception):
	def __init__(self,attribute,dependancy):
		print 'Error: Value not specified for Attribute:' + attribute.name+', dependant Attributes:' + str(dependancy) + ' are necessary'