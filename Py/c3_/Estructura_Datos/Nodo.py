import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')
G.add_node('G')

G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('B', 'E')
G.add_edge('C', 'F')
G.add_edge('C', 'G')

nx.draw(G, with_labels=True)
plt.show()