import itertools
from collections import defaultdict

class Graph:
    def __init__(self,vertices,terminals,edges):
        self.V= vertices #No. of vertices
        self.T = terminals #No. of terminal nodes, must be first x nodes
        self.Edges = edges
        self.SteinerGraph = [] # default dictionary to store graph
    def steinerTree(self):
        nonterminals = range(self.T,self.V)
        edgeadded = False
        print (nonterminals)
        minWeight = 100000000
        minTree = []
        #loop through all the possible numbers of additional vertices
        k = 0
        while k <= len(nonterminals):
            print ("K: " + str(k) + " len(nonterminals): " + str(len(nonterminals) ))
        # find all possible subsets of vertices of the specified size
            combinations = list(itertools.combinations(nonterminals, k))
            for c in combinations:
                # create a graph from one of the combinations
                g = SubGraph(self.V)
                terminals = list(range(0,self.T))
                vSet = set(list(c)  + terminals)
                # only add edges between nodes included in the subgraph
                for v1,v2,w in self.Edges:
                    if (int(v1) in vSet) and (int(v2) in vSet):
                        edgeadded = True
                        g.addEdge(v1,v2,w)
                if (edgeadded):
                    candidateTree, candidateWeight = g.KruskalMST()
                    if candidateWeight < minWeight:
                        minWeight = candidateWeight
                        minTree = candidateTree
                edgeadded = False
            k += 1
        print ("minWeight: " + str(minWeight))
        print ("minTree:")
        for u,v,weight in minTree:
            print (str(u) + " -- " + str(v) + " == " + str(weight))


# Code for Kruskal's adapted from Neelam Yadav on geekforgeek.com

#Class to represent a subgraph candidate
class SubGraph:

    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary
        # to store graph


    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

    # If ranks are same, then make one as root
    # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):

        resultTree =[] #This will store the resultant MST
        resultWeight = 0

        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

    # Step 1: Sort all the edges in non-decreasing
    # order of their
    # weight. If we are not allowed to change the
    # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,key=lambda item: item[2])

        parent = [] ; rank = []

    # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

    # Number of edges to be taken is equal to V-1
        if len(self.graph) > 0:
            while e < self.V -1 :

        # Step 2: Pick the smallest edge and increment
        # the index for next iteration
                if i >= len(self.graph):
                    break;
                u,v,w = self.graph[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent ,v)

        # If including this edge does't cause cycle,
        # include it in result and increment the index
        # of result for next edge
                if x != y:
                    e = e + 1
                    resultTree.append([u,v,w])
                    resultWeight += w
                    self.union(parent, rank, x, y)
            return resultTree, resultWeight
        # Else discard the edge


steinergraph = Graph(4,3,[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)])
steinergraph.steinerTree()

steinergraph2 = Graph(4,2,[(0,2,5),(1,2,20),(0,3,2),(1,3,10)])
steinergraph2.steinerTree()
