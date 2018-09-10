import pandas as pd
class Output():
	def __init__(self,outputFileName,outputData,verbose):
		self.outputFile = open(outputFileName,'w')
		self.outputData = pd.DataFrame(outputData)
		self.verbose = verbose
	def createOutputFile(self):
		index = range(len(self.outputData.columns))
		index[0] = 'id'
		index[-1] = 'classification'
		self.outputData.columns = index
		
		#self.outputData.columns[0] = 'id'
		#self.outputData.columns[-1] = 'classification'	
		if self.verbose > 0:
			print 'Creating output file: ' + str(self.outputFile.name)
		self.outputData.to_csv(self.outputFile,index=False)
