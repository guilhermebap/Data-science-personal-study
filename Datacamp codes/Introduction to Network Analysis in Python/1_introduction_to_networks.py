'''
In this chapter, you'll be introduced to fundamental concepts in network
analytics while exploring a real-world Twitter network dataset. You'll also
learn about NetworkX, a library that allows you to manipulate, analyze, and
model graph data. You'll learn about the different types of graphs and how to
rationally visualize them.
'''


'''
Basic drawing of a network using NetworkX
'''
# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt

# Draw the graph to screen
nx.draw(T_sub)
plt.show()




'''
Queries on a graph
'''
# Use a list comprehension to get the nodes of interest: noi
noi = [n for n, d in T.nodes(data=True) if d['occupation'] == 'scientist']

# Use a list comprehension to get the edges of interest: eoi
eoi = [(u, v) for u, v, d in T.edges(data=True) if d['date'] < date(2010, 1, 1)]




'''
Specifying a weight on edges
'''
# Set the weight of the edge
T.edges[1,10]['weight'] = 2

# Iterate over all the edges (with metadata)
for u, v, d in T.edges(data=True):

    # Check if node 293 is involved
    if 293 in [u,v]:

        # Set the weight to 1.1
        T.edges[u,v]['weight'] = 1.1




'''
Checking whether there are self-loops in the graph
'''
# Define find_selfloop_nodes()
def find_selfloop_nodes(G):
    """
    Finds all nodes that have self-loops in the graph G.
    """
    nodes_in_selfloops = []

    # Iterate over all the edges of G
    for u, v in G.edges():

    # Check if node u and node v are the same
        if u == v:

            # Append node u to nodes_in_selfloops
            nodes_in_selfloops.append(u)

    return nodes_in_selfloops

# Check whether number of self loops equals the number of nodes in self loops
assert T.number_of_selfloops() == len(find_selfloop_nodes(T))




'''
Visualizing using Matrix plots

It is time to try your first "fancy" graph visualization method: a matrix plot.
To do this, nxviz provides a MatrixPlot object.

nxviz is a package for visualizing graphs in a rational fashion. Under the hood,
the MatrixPlot utilizes nx.to_numpy_matrix(G), which returns the matrix form of
the graph. Here, each node is one column and one row, and an edge between the
two nodes is indicated by the value 1. In doing so, however, only the weight
metadata is preserved; all other metadata is lost, as you'll verify using an
assert statement.

A corresponding nx.from_numpy_matrix(A) allows one to quickly create a graph
from a NumPy matrix. The default graph type is Graph(); if you want to make it
a DiGraph(), that has to be specified using the create_using keyword argument,
e.g. (nx.from_numpy_matrix(A, create_using=nx.DiGraph)).
'''
# Import nxviz
import nxviz as nv

# Create the MatrixPlot object: m
m = nv.MatrixPlot(T)

# Draw m to the screen
m.draw()

# Display the plot
plt.show()

# Convert T to a matrix format: A
A = nx.to_numpy_matrix(T)

# Convert A back to the NetworkX form as a directed graph: T_conv
T_conv = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

# Check that the `category` metadata field is lost from each node
for n, d in T_conv.nodes(data=True):
    assert 'category' not in d.keys()



'''
Visualizing using Circos plots

Circos plots are a rational, non-cluttered way of visualizing graph data, in
which nodes are ordered around the circumference in some fashion, and the edges
are drawn within the circle that results, giving a beautiful as well as
informative visualization about the structure of the network.
'''
# Import necessary modules
import matplotlib.pyplot as plt
from nxviz import CircosPlot

# Create the CircosPlot object: c
c = CircosPlot(T)

# Draw c to the screen
c.draw()

# Display the plot
plt.show()




'''
Visualizing using Arc plots

Following on what you've learned about the nxviz API, now try making an
ArcPlot of the network. Two keyword arguments that you will try here are
node_order='keyX' and node_color='keyX', in which you specify a key in the node
metadata dictionary to color and order the nodes by.
'''
# Import necessary modules
import matplotlib.pyplot as plt
from nxviz import ArcPlot

# Create the un-customized ArcPlot object: a
a = ArcPlot(T)

# Draw a to the screen
a.draw()

# Display the plot
plt.show()

# Create the customized ArcPlot object: a2
a2 = ArcPlot(T, node_order='category', node_color='category')

# Draw a2 to the screen
a2.draw()

# Display the plot
plt.show()
