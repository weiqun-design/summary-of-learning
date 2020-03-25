import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
for edge in edges:
    G.add_edge(edge[0],edge[1])
layout = nx.spring_layout(G)
nx.draw(G,pos=layout,with_labels=True,hold=False)
pagerank_list = nx.pagerank(G,alpha=1)
plt.show()
print(pagerank_list)
pr = nx.pagerank(G,alpha=0.85)
print(pr)