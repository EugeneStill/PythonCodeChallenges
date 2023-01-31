import unittest
import collections

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class CloneGraph(unittest.TestCase):
    """
    For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

    An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

    The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    """

    def clone_graph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # DFS Iterative
        if not node:
            return node
        m, visited, stack = dict(), set(), collections.deque([node])
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                stack.append(neigh)
        return m[node]

    def test_cg(self):
        # work on tests after reviewing sections on graphs
        # this challenge came from the DFS Stack section
        return



