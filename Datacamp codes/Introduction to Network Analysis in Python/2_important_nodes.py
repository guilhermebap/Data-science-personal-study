'''
You'll learn about ways to identify nodes that are important in a network. In
doing so, you'll be introduced to more advanced concepts in network analysis as
well as the basics of path-finding algorithms. The chapter concludes with a deep
dive into the Twitter network dataset which will reinforce the concepts you've
learned, such as degree centrality and betweenness centrality.
'''


'''
Compute number of neighbors for each node
'''
# Define nodes_with_m_nbrs()
def nodes_with_m_nbrs(G, m):
    """
    Returns all nodes in graph G that have m neighbors.
    """
    nodes = set()

    # Iterate over all nodes in G
    for n in G.nodes():

        # Check if the number of neighbors of n matches m
        if len(list(G.neighbors(n))) == m:

            # Add the node n to the set
            nodes.add(n)

    # Return the nodes with m neighbors
    return nodes

# Compute and print all nodes in T that have 6 neighbors
six_nbrs = nodes_with_m_nbrs(T, 6)
print(six_nbrs)




'''
Compute degree distribution

The number of neighbors that a node has is called its "degree", and it's
possible to compute the degree distribution across the entire graph. In this
exercise, your job is to compute the degree distribution across T.
'''
# Compute the degree of every node: degrees
degrees = [len(list(T.neighbors(n))) for n in T.nodes()]

# Print the degrees
print(degrees)




'''
Degree centrality distribution

Degree centrality distribution
The degree of a node is the number of neighbors that it has. The degree
centrality is the number of neighbors divided by all possible neighbors that it
could have. Depending on whether self-loops are allowed, the set of possible
neighbors a node could have could also include the node itself.

The nx.degree_centrality(G) function returns a dictionary, where the keys are
the nodes and the values are their degree centrality values.

The degree distribution degrees you computed in the previous exercise using the
list comprehension has been pre-loaded.
'''
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Compute the degree centrality of the Twitter network: deg_cent
deg_cent = nx.degree_centrality(T)

# Plot a histogram of the degree centrality distribution of the graph.
plt.figure()
plt.hist(list(deg_cent.values()))
plt.show()

# Plot a histogram of the degree distribution of the graph
plt.figure()
plt.hist(degrees)
plt.show()

# Plot a scatter plot of the centrality distribution and the degree distribution
plt.figure()
plt.scatter(x=degrees, y=list(deg_cent.values()))
plt.show()




'''
