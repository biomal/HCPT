from Settings import Settings 
from Hierarchy import Hierarchy
from FeatureExtractor import FeatureExtractor
from Input import Input
from Output import Output
import sys
class Parser:
	sectionsName = ['General','Data','Features','Hierarchy']
	featureTypes = ['Kmer','Reverse','PSEDNC','PSEKNC','PCPSEDNC','PCPSETNC','SCPSEDNC','SCPSETNC','DAC','DCC','DACC','TAC','TCC','TACC']
	def __init__(self,filename):
		self.settings = Settings()
		self.lineCounter = 0
		file = open(filename,'r')
		self.lines = file.readlines()	
		self.fileSize = len(self.lines)
		while self.lineCounter < self.fileSize:
			name = self.parseSectionName(self.getLine())
			self.parseSection(name)
			# break
		self.checkMandatoryAttributes()
		verbose = self.settings.getSection('General').getAttributeValue('Verbose').value
		hierarchy = Hierarchy(self.settings.getSection('Hierarchy').getAttributeValue('File').value,verbose)			
		featureExtrator = FeatureExtractor(self.settings.getSection('Features').getAttributeValue('Type').value,self.getFeatureExtractorParameters(),hierarchy,verbose)
		inputData = Input(self.settings.getSection('Data').getAttributeValue('Input').value,verbose).getParsedData()
		outputData = featureExtrator.getFeatures(inputData)
		output = Output(self.settings.getSection('Data').getAttributeValue('Output').value,outputData,verbose)
		output.createOutputFile()
		
	def parseSectionName(self,name):
		sectionName = name.strip()[1:-1] 
		if sectionName not in self.sectionsName:
			try:
				Error = ValueError()
				Error.msg = 'Error Section:' + sectionName + ' not valid, the available Sections are ' + str(self.sectionsName)
				raise Error
			except ValueError as e:
				 print("Section not found error:", e.msg)
				 sys.exit(1)

		return sectionName
	def getLine(self):
		if self.lineCounter < self.fileSize:
			return self.lines[self.lineCounter]
		return None
	def increaseLineCounter(self):
		self.lineCounter+=1
	def parseSection(self,name):
		section = self.settings.getSection(name)
		self.increaseLineCounter()
		while not self.isSectionName(self.getLine()):
			line = self.getLine()
			parsedLine = self.parseLine(line,name)
			self.increaseLineCounter()
			section.setAttributeValue(parsedLine[0],parsedLine[1])
		# section.toString()	
	def parseLine(self,line,sectionName):
		splitLine = [l.strip() for l in line.split('=')]
		splitLine[1] = self.convertStringValue(splitLine[1]) 
		return (splitLine[0],splitLine[1])
	def isSectionName(self,line):
		if line is None:
			return True
		line = line.strip()
		return line.startswith('[') and line.endswith(']')
	def convertStringValue(self,value):
		if value == 'False':
			return False
		elif value == 'True':
			return True
		elif value.startswith('[') and value.endswith(']'):
			value = value[1:-1].split(',')
			for i in xrange(len(value)):
				try:
					floatSuccess = False
					floatTry = float(value[i])
					floatSuccess = True				
					intTry = int(value[i])
					if floatTry == intTry:
						value[i] = intTry
					else:
						value[i] = floatTry
				except:
					if floatSuccess:
						value[i] = floatTry
		else:
			try:
				floatSuccess = False
				floatTry = float(value)
				floatSuccess = True				
				intTry = int(value)
				if floatTry == intTry:
					return intTry
				else:
					return floatTry
			except:
				if floatSuccess:
					return floatTry
		return value			  	
	def checkMandatoryAttributes(self):
		featureSection = self.settings.getSection('Features')
		if not featureSection.getAttributeValue('Type').enabled:
			print 'Error: Necessary to specify type of feature to be extracted'
		elif featureSection.getAttributeValue('Type').value not in self.featureTypes:
			print 'Error: Invalid Feature type: ' + str(featureSection.getAttributeValue('Type').value) + ' available types are ' + str(self.featureTypes)
		dataSection = self.settings.getSection('Data')	
		if not dataSection.getAttributeValue('Input').enabled:
			print 'Error: Necessary to specify input settings file'
		elif not dataSection.getAttributeValue('Output').enabled:
			print 'Error: Necessary to specify output file name'
		hierarchySection = self.settings.getSection('Hierarchy')
		if not dataSection.getAttributeValue('Output').enabled:
			print 'Error: Necessary to specify hierarchy file settings'
	def getFeatureExtractorParameters(self):
		return self.settings.getSection('Features').attributes
	def getFeatures(self):
		return self.featureExtrator.getFeatures()
