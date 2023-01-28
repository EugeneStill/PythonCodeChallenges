import heapq
import unittest


# This class represents a directed graph using adjacency list representation
class Graph(object):
    def __init__(self, V: int):
        self.V = V
        self.graph = [[] for _ in range(V)]

    def addEdge(self, u: int, v: int, w: int):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))


    def shortestPath(self, src: int):
        # Create a priority queue to store vertices that are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))

        # Create a vector for distances and initialize all distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0

        while pq:
            # The first value in pair is the minimum distance from source to vertex at the time vertex was added to q
            # vertex is second value in pair
            d, current_vertex = heapq.heappop(pq)

            # use i to get all adjacent vertices of a vertex
            for neighbor, weight in self.graph[current_vertex]:
                # update distance from source to neighbor if path to neighbor through current_vertex is shorter
                if dist[neighbor] > dist[current_vertex] + weight:
                    # Updating distance of neighbor
                    dist[neighbor] = dist[current_vertex] + weight
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        print("RESULTS:")
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")
        return dist


class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        """verify shortest path from start to each node in graph"""
        # create the graph
        V = 9
        g = Graph(V)
        g.addEdge(0, 1, 4)
        g.addEdge(0, 7, 8)
        g.addEdge(1, 2, 8)
        g.addEdge(1, 7, 11)
        g.addEdge(2, 3, 7)
        g.addEdge(2, 8, 2)
        g.addEdge(2, 5, 4)
        g.addEdge(3, 4, 9)
        g.addEdge(3, 5, 14)
        g.addEdge(4, 5, 10)
        g.addEdge(5, 6, 2)
        g.addEdge(6, 7, 1)
        g.addEdge(6, 8, 6)
        g.addEdge(7, 8, 7)
        expected_result = [0, 4, 12, 19, 21, 11, 9, 8, 14]
        self.assertEqual(g.shortestPath(0), expected_result)

