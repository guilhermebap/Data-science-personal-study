'''
In this final chapter of the course, you'll consolidate everything you've learned
through an in-depth case study of GitHub collaborator network data. This is a
great example of real-world social network data, and your newly acquired skills
will be fully tested. By the end of this chapter, you'll have developed your
very own recommendation system to connect GitHub users who should collaborate
together.
'''


'''
Characterizing the network (II)
'''
# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.degree_centrality(G).values()))
plt.show()



'''
Characterizing the network (III)
'''
# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.betweenness_centrality(G).values()))
plt.show()



'''
MatrixPlot
'''
# Import necessary modules
from nxviz import MatrixPlot
import matplotlib.pyplot as plt

# Calculate the largest connected component subgraph: largest_ccs
largest_ccs = sorted(list(nx.connected_component_subgraphs(G)), key=lambda x: len(x))[-1]

# Create the customized MatrixPlot object: h
h = MatrixPlot(largest_ccs, node_grouping='grouping')

# Draw the MatrixPlot to the screen
h.draw()
plt.show()



'''
ArcPlot
'''
# Import necessary modules
from nxviz.plots import ArcPlot
import matplotlib.pyplot as plt

# Iterate over all the nodes in G, including the metadata
for n, d in G.nodes(data=True):

    # Calculate the degree of each node: G.node[n]['degree']
    G.node[n]['degree'] = nx.degree(G, n)

# Create the ArcPlot object: a
a = ArcPlot(G, node_order='degree')

# Draw the ArcPlot to the screen
a.draw()
plt.show()



'''
CircosPlot
'''
# Import necessary modules
from nxviz import CircosPlot
import matplotlib.pyplot as plt

# Iterate over all the nodes, including the metadata
for n, d in G.nodes(data=True):

    # Calculate the degree of each node: G.node[n]['degree']
    G.node[n]['degree'] = nx.degree(G, n)

# Create the CircosPlot object: c
c = CircosPlot(G, node_order='degree', node_color='grouping', node_grouping='grouping')

# Draw the CircosPlot object to the screen
c.draw()
plt.show()



'''
Finding cliques (I)

cliques are "groups of nodes that are fully connected to one another", while a
maximal clique is a clique that cannot be extended by adding another node in the
graph.
'''
# Calculate the maximal cliques in G: cliques
cliques = nx.find_cliques(G)

# Count and print the number of maximal cliques in G
print(len(list(cliques)))



'''
Finding cliques (II)
'''
# Import necessary modules
import networkx as nx
from nxviz import CircosPlot
import matplotlib.pyplot as plt

# Find the author(s) that are part of the largest maximal clique: largest_clique
largest_clique = sorted(nx.find_cliques(G), key=lambda x:len(x))[-1]

# Create the subgraph of the largest_clique: G_lc
G_lc = G.subgraph(largest_clique)

# Create the CircosPlot object: c
c = CircosPlot(G_lc)

# Draw the CircosPlot to the screen
c.draw()
plt.show()



'''
Finding important collaborators

You'll now look at important nodes once more. Here, you'll make use of the
degree_centrality() and betweenness_centrality() functions in NetworkX to
compute each of the respective centrality scores, and then use that information
to find the "important nodes".
'''
# Compute the degree centralities of G: deg_cent
deg_cent = nx.degree_centrality(G)

# Compute the maximum degree centrality: max_dc
max_dc = max(deg_cent.values())

# Find the user(s) that have collaborated the most: prolific_collaborators
prolific_collaborators = [n for n, dc in deg_cent.items() if dc == max_dc]

# Print the most prolific collaborator(s)
print(prolific_collaborators)




'''
Characterizing editing communities
'''
