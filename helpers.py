import networkx as nx
import pickle
#import plotly.plotly as py
import random
#from plotly.graph_objs import *
#from plotly.offline import init_notebook_mode, plot, iplot
#init_notebook_mode(connected=True)

class Map:
	def __init__(self, G):
		self._graph = G
		self.intersections = nx.get_node_attributes(G, "pos")
		self.roads = [list(G[node]) for node in G.nodes()]

	def save(self, filename):
		with open(filename, 'wb') as f:
			pickle.dump(self._graph, f)

def load_map(name):
	with open(name, 'rb') as f:
		G = pickle.load(f)
	return Map(G)

