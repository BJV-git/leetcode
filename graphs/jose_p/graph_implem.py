# class vertex:
#     def __init__(self, val):
#         self.val = val
#         self.connections={}
#
#     def addN(self, nbr_val, w=0):
#         self.connections[nbr_val] = w

from collections import defaultdict

class Graph(object):

    def __init__(self):
        self.graph = defaultdict(dict)

    def addVertex(self, value):
        self.graph[value]={}

    def getVertex(self, key):
        try:
            return self.graph[key]
        except:
            return None # or can also return False

    def addEdge(self,s,f,weight=0): # for now assuming the single directional graph

        if s not in self.graph:
            self.addVertex(s)

        if f not in self.graph:
            self.addVertex(f)

        self.graph[s].update({f:weight})

    def getVertices(self):
        return self.graph.keys()

    



a = Graph()

a.addVertex(5)

print(a.graph)

# a={1:2, 3:4}
#
# a.update({4:7})
#
# print(a)