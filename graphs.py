class Graph:
    def __init__(self):
        self.no_of_nodes = 0
        self.adjacentList = {}
    def addVertex(self, node):
        self.adjacentList[node] = []
    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        return
    
