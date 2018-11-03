# import queue as q
import Heap as h
PRIORITY = 0
PATH = 2
NODE= 1

class Graph:
    def __init__(self, Root=None, Directed=False):
        self.vertices = set(Root)
        self.edges = {}
        self.isDirected = Directed
        if (Root is not None):
            self.edges[Root] = list()

    def addedge(self, From, To, priority):
        if (From in self.vertices and self.isDirected == False):
            self.edges[From].append((priority,To ))
        elif (self.isDirected == True):
            self.edges[From].append((priority,To))
            self.edges[To].append((priority,From ))

        else:
            raise Exception('Vertex not in graph')

    def addvertex(self, vertex):
        if (vertex in self.vertices):
            raise Exception('Vertex is already in graph')
        else:
            self.vertices.add(vertex)
            self.edges[vertex] = list()

    def createVisitedNodes(self):
        self.visitedNodes = dict.fromkeys(self.vertices, False)  # intializes all to false to begin

    def visitNode(self, node):
        self.visitedNodes[node] = True

    def __str__(self):
        return str(self.edges)

    def UCS(self, root, goal):
        pq = h.PriorityQueue()
        pq.enqueue((0, root, root))  # (priority, currnode, path)
        while (not (pq.empty())):  # iterates till queue is empty otherwise until all nodes are exhausted
            print(pq.queue)
            node = pq.dequeue()
            if (node[NODE] in goal):  # if the current node in queue is equal to goal then we have print path
                print(node[PATH] + " Cost: " + str(node[PRIORITY]))  # prints path
                break
            elif(self.visitedNodes[node[NODE]]):
                continue #next iteration node has already been expanded
            else:
                self.visitNode(node[NODE])
                children = self.edges[node[NODE]]

                for childnode in children:
                    if (self.visitedNodes[childnode[NODE]] is not True):
                        pq.enqueue((childnode[PRIORITY] + node[PRIORITY], childnode[NODE], node[PATH] + "->" + str(childnode[NODE])))  # enques all of the node children
                    else:
                        continue
















