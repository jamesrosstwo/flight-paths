"""
Note to self:
Make a class for each node containing location, name, and a distance_to method.
"""

import collections
import math


class Map:
    @staticmethod
    def distance_between(a, b):
        return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    def __init__(self):
        self.vertices = set()
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, start, end, weight):
        self.edges[start].append(end)
        self.weights[(start, end)] = weight

    def add_bidirectional_edge(self, a, b, weight):
        if b not in self.edges[a]:
            self.edges[a].append(b)
            self.weights[(a, b)] = weight
        if a not in self.edges[b]:
            self.edges[b].append(a)
            self.weights[(b, a)] = weight

    def dijkstra(self, start):
        q = set()
        d = dict.fromkeys(list(self.vertices), math.inf)
        prev = dict.fromkeys(list(self.vertices), None)
        d[start] = 0

        while q != self.vertices:
            v = min((set(d.keys()) - q), key=d.get)
            for neighbor in set(self.edges[v]) - q:
                new_path = d[v] + self.weights[v, neighbor]
                if new_path < d[neighbor]:
                    d[neighbor] = new_path
                    prev[neighbor] = v
            q.add(v)
        return d, prev

    def shortest_path(self, start, end):
        path = self.dijkstra(start)[1]
        out = []
        current = end
        flag = False
        while current is not None:
            out.append(current)
            current = path[current]
            if current == start:
                flag = True
        if flag:
            out.reverse()
            return out
        return []
