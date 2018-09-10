from repDNA.nac import Kmer
from repDNA.nac import RevcKmer 

from repDNA.ac import DAC 
from repDNA.ac import DCC 
from repDNA.ac import DACC
from repDNA.ac import TAC 
from repDNA.ac import TCC
from repDNA.ac import TACC
from repDNA.psenac import PseDNC
from repDNA.psenac import PseKNC 
from repDNA.psenac import PCPseDNC
from repDNA.psenac import PCPseTNC
from repDNA.psenac import SCPseDNC
from repDNA.psenac import SCPseTNC
from repDNA.util import normalize_index

from AttributeDependancyException import AttributeDependancyException
from AttributeMissingException import AttributeMissingException
class FeatureExtractor:
	def __init__(self,name,parameters,hierarchy,verbose):
		self.name = name
		self.parameters = parameters
		self.hierarchy = hierarchy
		self.verbose = verbose
		if self.name == 'Kmer':
			self.extractor = Kmer(k=self.parameters['K'].value,upto=self.parameters['UpTo'].value,normalize = self.parameters['Normalize'].value)
		elif self.name == 'Reverse':
			self.extractor = RevcKmer(k=self.parameters['K'].value,upto=self.parameters['UpTo'].value,normalize = self.parameters['Normalize'].value) 
		elif self.name == 'DAC':
			self.extractor = DAC(lag = self.parameters['Lag'].value) 
		elif self.name == 'DCC':
			self.extractor = DCC(lag = self.parameters['Lag'].value)
		elif self.name == 'DACC':
			self.extractor = DACC(lag = self.parameters['Lag'].value) 
		elif self.name == 'TAC':
			self.extractor = TAC(lag = self.parameters['Lag'].value) 
		elif self.name == 'TCC':
			self.extractor = TCC(lag = self.parameters['Lag'].value)
		elif self.name == 'TACC':
			self.extractor = TACC(lag = self.parameters['Lag'].value)
		elif self.name == 'PSEDNC':
			self.extractor = PseDNC(lamada = self.parameters['Lamada'].value, w = self.parameters['W'].value)
		elif self.name == 'PSEKNC':
			self.extractor = PseKNC(lamada = self.parameters['Lamada'].value, w = self.parameters['W'].value)
		elif self.name == 'PCPSEDNC':
			self.extractor = PCPseDNC(lamada = self.parameters['Lamada'].value, w = self.parameters['W'].value)
		elif self.name == 'PCPSETNC':
			self.extractor = PCPseTNC(lamada = self.parameters['Lamada'].value, w = self.parameters['W'].value) 
		elif self.name == 'SCPSEDNC':
			self.extractor = SCPseDNC(lamada = self.parameters['Lamada'].value, w = self.parameters['W'].value) 
		elif self.name == 'SCPSETNC':
			self.extractor = SCPseTNC(lamada = self.parameters['Lamada'].value, w = self.parameters['W'].value)
		self.checkParameters()
		# print self.extractFeature(['ACTG'])
	def getFeatures(self,sequences):
		if self.verbose > 0:
			counter = 1
		features = []
		for sequence in sequences:
			if self.verbose > 0:
				print 'Extracting Features for sequence number ' + str(counter) + ' of ' + str(len(sequences)) + ' sequences'
				counter+=1
			line = [sequence[0]]
			line.extend(self.extractFeature(sequence[2]))			
			line.append(self.hierarchy.getNumericalName(sequence[1]))
			features.append(line)
		return features
	def extractFeature(self,sequence):
		if self.name == 'Kmer':
			return self.extractor.make_kmer_vec(sequence)[0]
		elif self.name == 'Reverse':
			return self.extractor.make_revckmer_vec(sequence)[0] 
		elif self.name == 'DAC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_dac_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0] 
				else:		
					return self.extractor.make_dac_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_dac_vec(sequence,all_property=True)[0] 	
		elif self.name == 'DCC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_dcc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0] 
				else:		
					return self.extractor.make_dcc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_dcc_vec(sequence,all_property=True)[0]		
		elif self.name == 'DACC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_dacc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0] 
				else:		
					return self.extractor.make_dacc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_dacc_vec(sequence,all_property=True)[0]
		elif self.name == 'TAC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_tac_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0] 
				else:		
					return self.extractor.make_tac_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_tac_vec(sequence,all_property=True)[0]
		elif self.name == 'TCC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_tcc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0] 
				else:		
					return self.extractor.make_tcc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_tcc_vec(sequence,all_property=True)[0]
		elif self.name == 'TACC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_tacc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0]  
				else:		
					return self.extractor.make_tacc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_tacc_vec(sequence,all_property=True)[0]
		elif self.name == 'PSEDNC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_psednc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0]  
				else:		
					return self.extractor.make_psednc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_psednc_vec(sequence)[0]
		elif self.name == 'PSEKNC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_pseknc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0]  
				else:		
					return self.extractor.make_pseknc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_pseknc_vec(sequence)[0]
		elif self.name == 'PCPSEDNC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_pcpsednc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0]  
				else:		
					return self.extractor.make_pcpsednc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_pcpsednc_vec(sequence,all_property=True)[0]
		elif self.name == 'PCPSETNC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_pcpsetnc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0]  
				else:		
					return self.extractor.make_pcpsetnc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_pcpsetnc_vec(sequence,all_property=True)[0]
		elif self.name == 'SCPSEDNC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_scpsednc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0]  
				else:		
					return self.extractor.make_scpsednc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_scpsednc_vec(sequence,all_property=True)[0]
		elif self.name == 'SCPSETNC':
			if self.parameters['PhycheIndex'].enabled:
				if self.parameters['ExtraIndex'].enabled:
					return self.extractor.make_scpsetnc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value,extra_phyche_index = normalize_index(self.parameters['ExtraIndex'].value ,is_convert_dict=True))[0]  
				else:		
					return self.extractor.make_scpsetnc_vec(sequence,phyche_index = self.parameters['PhycheIndex'].value)[0] 
			else:
				return self.extractor.make_scpsetnc_vec(sequence,all_property=True)[0]			
	def checkParameters(self):
		if self.verbose > 0:
			if self.name == 'Kmer' or self.name == 'Reverse':
				if not self.parameters['K'].enabled:
					self.printDefaultValueWarning(self.name,self.parameters['K'].value)
				if not self.parameters['UpTo'].enabled:
					self.printDefaultValueWarning(self.name,self.parameters['UpTo'].value)
				if not self.parameters['Normalize'].enabled:
					self.printDefaultValueWarning(self.name,self.parameters['Normalize'].value)
			elif self.name == 'DAC' or self.name == 'DCC' or self.name == 'DACC' or self.name == 'TAC' or self.name == 'TCC' or self.name == 'TACC':
				if self.parameters['AllProperty'].enabled and self.parameters['AllProperty'].value:
					self.printAutoDisableWarning(self.parameters['AllProperty'],['PhycheIndex','ExtraIndex']) 
				elif self.parameters['ExtraIndex'].enabled and not self.parameters['PhycheIndex'].enabled:
					raise AttributeDependancyException(self.parameters['ExtraIndex'],['PhycheIndex'])
				elif not self.parameters['PhycheIndex'].enabled:
					self.printDefaultValueWarning(self.name,'AllProperty = ' + str(self.parameters['AllProperty'].value))
			elif self.name == 'PSEDNC' or self.name == 'PSEKNC' or self.name == 'PCPSEDNC' or self.name == 'PCPSETNC' or self.name == 'SCPSEDNC' or self.name == 'SCPSETNC':
				if not self.parameters['Lamada'].enabled:
					self.printDefaultValueWarning(self.name,'Lamada = ' + str(self.parameters['Lamada'].value))
				if not self.parameters['W'].enabled:
					self.printDefaultValueWarning(self.name,'W = ' + str(self.parameters['W'].value))
	def printDefaultValueWarning(self,feature,attributes):
		print 'Warning: Value not specified for Feature Type:' + feature + ', using default parameter: ' + str(attributes)
	def printAutoDisableWarning(self,attribute,disabled):
		print 'Warning: Value specified for Attribute:' + attribute.name + ', other Attributes: ' + str(disabled) + ' are disabled'
