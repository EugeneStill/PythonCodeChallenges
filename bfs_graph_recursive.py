from collections import deque
import helpers.graph as graph_class
### this came from Google study material but doesn't seem like its really recrursive.
### also seems strange how much of the traversal is built into the driver code

# Perform BFS recursively on the graph (NOTE: Iterative approach for BFS is recommended)
def recursiveBFS(graph, q, discovered):
    if not q:
        return

    # dequeue front node and print it
    v = q.popleft()
    print(v, end=' ')

    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            # mark it as discovered and enqueue it
            discovered[u] = True
            q.append(u)

    recursiveBFS(graph, q, discovered)


if __name__ == '__main__':

    # List of graph edges as per the above diagram
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13, and 14 are single nodes
    ]

    # total number of nodes in the graph (labelled from 0 to 14)
    n = 15

    # build a graph from the given edges
    graph = graph_class.Graph(edges, n)

    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n

    # create a queue for doing BFS
    q = deque()

    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            # mark the source vertex as discovered
            discovered[i] = True

            # enqueue source vertex
            q.append(i)

            # start BFS traversal from vertex i
            recursiveBFS(graph, q, discovered)

#
# """
# OUTPUT
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# """