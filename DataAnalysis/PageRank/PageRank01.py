import networkx as nx

G = nx.DiGraph()  # 创建有向图
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("B", "D"), ("C", "A"), ("D", "B"), ("D", "C")]
for edge in edges:
    G.add_edge(edge[0], edge[1])
pagerank_list = nx.pagerank(G,alpha=0.85)
print(pagerank_list)
