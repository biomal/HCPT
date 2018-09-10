import sys
class Input:
	def __init__(self,inputFileName,verbose):
		self.inputFileData = open(inputFileName,'r').readlines()
		self.parsedData = []
		self.parseInputFile(verbose)
	def parseInputFile(self,verbose):
		size = len(self.inputFileData)
		lineCounter = 0 
		while lineCounter < size:
			if verbose > 0:
				print 'Parsing input data number ' + str(lineCounter/2 + 1) + ' of ' + str(size/2) 
			inputId = self.inputFileData[lineCounter].split('|')[0][1:]
			inputLabel = self.inputFileData[lineCounter].split('|')[1].strip()
			lineCounter+=1
			if len(self.inputFileData[lineCounter].strip()) == 0:
				try:
					Error = ValueError()
					Error.msg = 'Error in line: ' + str(lineCounter + 1) + ', input data number: ' + str((lineCounter + 1 )/2 + 1) + ': Empty Sequence'
					raise Error
				except ValueError as e:
					print("Attribute value error:", e.msg)
					sys.exit(1)
			inputSequence = self.inputFileData[lineCounter].strip()
			lineCounter+=1
			self.parsedData.append((inputId,inputLabel,[inputSequence]))
	def getParsedData(self):
		return self.parsedData