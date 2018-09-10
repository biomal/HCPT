from Section import Section 
import networkx as nx
class Hierarchy:
	G=nx.DiGraph()
	def __init__(self,hierarchyFile,verbose):
		self.G.add_node('0', depth = 0, name = 'Root')
		n = open(hierarchyFile,'r')
		for line in n.readlines():
			nodeName = line.split('=')[0].strip()
			numerical = line.split('=')[1].strip()
			self.buildHierarchy(nodeName,numerical)
		if verbose > 0:
			print 'Hierarchy initialized with ' + str(len(self.G.nodes()) - 1) + ' nodes'	
	def buildHierarchy(self,line,numerical):
		node_name=""
		edge_name=""
		nodes = []
		edges = []
		edges.append(['0',line.split('.')[0]])	
		for i in line.split('.'):
			node_name+= i
			self.G.add_node(node_name, depth = len(node_name.split('.')))
			node_name+= '.'
		aux = []
		edge_name=line.split('.')[0]
		aux.append(edge_name)
		for i in range(len(line.split('.'))-1):
			edge_name+= '.'
			edge_name+= line.split('.')[i+1]
			aux.append(edge_name)			
			edges.append(aux)
			aux = []
			aux.append(edge_name)
		self.G.add_edges_from(edges)
		# self.G[line]['numerical'] = numerical
		self.G.add_node(line, depth = len(line.split('.')) , numerical = numerical)
	def getNumericalName(self,nodeName):
		return self.G.node[nodeName]['numerical']