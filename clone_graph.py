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

    def clone_graph_dfs(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # DFS Iterative
        if not node:
            return node
        # set up empty dic for new graph, set for visited and stack to process nodes starting with input node
        new_graph, visited, stack = {}, set(), collections.deque([node])
        # use stack to iteratre through all nodes and build out new_graph
        while stack:
            # pop last added node and skip it if already visited
            n = stack.pop()
            if n in visited:
                continue
            # add node to visited
            visited.add(n)
            # add node to new_graph if not present
            if n not in new_graph:
                new_graph[n] = Node(n.val)
            # for each of node's neighbors check to see if neighbor node need to be added to graph
            for neigh in n.neighbors:
                if neigh not in new_graph:
                    new_graph[neigh] = Node(neigh.val)
                # add neighbor node to list of node's neighbors
                new_graph[n].neighbors.append(new_graph[neigh])
                # add neighbor node to the stack
                stack.append(neigh)
        return new_graph[node]

    def clone_graph_bfs(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # BFS Iterative
        if not node:
            return node

        q, clones = collections.deque([node]), {node.val: Node(node.val, [])}
        while q:
            # pop oldest node from q
            cur = q.popleft()

            # for all of cur's neighbors
            for ngbr in cur.neighbors:
                # if neighbor not in clones, add it to clones and append to q
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                # add the neighbor's val to current clone's list of neighbors
                clones[cur.val].neighbors.append(clones[ngbr.val])

        return clones[node.val]

    def test_cg(self):
        # work on tests after reviewing sections on graphs
        # this challenge came from the DFS Stack section
        return



