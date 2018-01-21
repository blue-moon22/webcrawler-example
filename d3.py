#### Draw network
import d3py
import networkx as nx
import logging
import csv
with open('output.csv', 'rb') as f:
    reader = csv.reader(f)
    allLinks = list(reader)

fromLinks = allLinks[0]
toLinks = allLinks[1]

logging.basicConfig(level=logging.DEBUG)

G = nx.Graph()
numbers = {}
total = list(set(fromLinks)) + list(set(toLinks))
for i in range(len(total)):
    numbers[total[i]] = i
for i in range(len(fromLinks)):
    G.add_edge(numbers[fromLinks[i]],numbers[toLinks[i]])

# use 'with' if you are writing a script and want to serve this up forever
with d3py.NetworkXFigure(G, width=1200, height=700, host="localhost") as p:
    p += d3py.ForceLayout()
    p.show()
