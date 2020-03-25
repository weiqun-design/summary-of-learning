import networkx as nx
from networkx.algorithms import community
G = nx.read_gml('./football.gml')
communities = list(community.label_propagation_communities(G))
print(communities)