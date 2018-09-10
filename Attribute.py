import sys
class Attribute:
	name = None
	value = None
	enabled = False
	category = None # 0 = int,1 = float,2 = string, 3 = boolean
	def __init__(self,name,value,category):
		self.name = name
		self.value = value
		self.category = category
	def enable(self):
		self.enabled = True
	def setValue(self,value):
		if self.checkCategory(value):
			self.value = value
			self.enabled = True
		else:
			try:
				Error = ValueError()
				Error.msg = 'Error in attribute: ' + self.name + ' expected type ' + str(self.category) + ', got ' + str(type(value))
				raise Error
			except ValueError as e:
				 print("Attribute value error:", e.msg)
				 sys.exit(1)
	def checkCategory(self,value):
		return self.category == type(value)
	# def isOK():
	# 	if self.mandatory:
	# 		if self.enabled:
	# 			return True
	# 		else:
	# 			print 'Value not specified for attribute:' + self.name + ' using default value:' + self.value	
	# 			return True
	def toString(self):
		print self.name
		print self.value
		print self.category
		print self.mandatory
		print '-------'