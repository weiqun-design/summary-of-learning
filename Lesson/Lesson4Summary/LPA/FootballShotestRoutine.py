import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml('./football.gml')
nx.draw(G, with_labels=True)
plt.show()
print(nx.shortest_path(G, source='Buffalo', target='Kent'))
print(nx.shortest_path(G, source='Buffalo', target='Rice'))