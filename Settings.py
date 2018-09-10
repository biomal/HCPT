from Section import Section 
class Settings:
	def __init__(self):
		self.sections = {}
		self.initializeDefault()
	def addSection(self,section):
		self.sections[section.name] = section
	def getSection(self,name):
		return self.sections[name]
	def initializeDefault(self):
		''' General Section'''
		section = Section('General')
		section.addAttribute('Verbose',0,int)
		# section.isOK()
		self.addSection(section)
		# section.toString()
		''' Data Section'''
		
		section = Section('Data')
		section.addAttribute('Input','',str)
		section.addAttribute('Output','',str)
		self.addSection(section)
		# section.toString()

		''' Features Section '''
		section = Section('Features')
		section.addAttribute('Type','',str)
		section.addAttribute('K',4,int)
		section.addAttribute('Normalize',False,bool)
		section.addAttribute('UpTo',False,bool)

		section.addAttribute('Lamada',3,int)
		section.addAttribute('W',0.005,float)

		section.addAttribute('AllProperty',True,bool)
		section.addAttribute('Lag',1,int)
		section.addAttribute('PhycheIndex',[],list)
		section.addAttribute('ExtraIndex',[],list)
				

		#ADICIONAR AKI OS OUTROS PARAMETROS DO ROLE
		self.addSection(section)
		# section.toString()

		''' Hierarchy Section'''			
		section = Section('Hierarchy')
		section.addAttribute('File','',str)
		self.addSection(section)
		# section.toString()

	def toString(self):
		for key, value in self.sections.iteritems():
			print 'Section key: ' + key 
			print 'Value'
			value.toString()
			print '-------'