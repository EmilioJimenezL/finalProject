import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph();

g.add_node(1);
g.add_node(2);

g.add_edge(1,2);

nx.draw(g, with_labels=True)
plt.show()