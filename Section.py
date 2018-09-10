from Attribute import Attribute
import sys
class Section:
	def __init__(self,name):
		self.name = name
		self.attributes = {}
	
	def addAttribute(self,name,value,category):
		attribute = Attribute(name,value,category)
		self.attributes[name] = attribute
	def getAttributeValue(self,name):
		return self.attributes[name]
	def setAttributeValue(self,name,value):
		if name not in self.attributes:
			try:
				Error = ValueError()
				Error.msg = 'Error Attribute:' + name + ' not valid in Section:' + self.name + ', the available Attributes are ' + str(self.attributes.keys())
				raise Error
			except ValueError as e:
				 print("Attribute value error:", e.msg)
				 sys.exit(1)
		else:
			self.attributes[name].setValue(value)
	# def isOK():
	# 	for key, value in self.attributes.iteritems():
			
	def toString(self):
		print self.name
		for key, value in self.attributes.iteritems():
			print 'Attribute key:' + str(key)
			print 'value:' 
			value.toString()
			print '-------'
