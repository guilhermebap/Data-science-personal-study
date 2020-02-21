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
