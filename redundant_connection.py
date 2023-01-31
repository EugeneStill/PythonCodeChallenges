import unittest
import collections


class FindRedundantConnection(unittest.TestCase):
    """
    build out a graph and return the first edge that makes a cycle in the graph
    """
    def find_redundant_connection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def dfs(u, v):
            print("CHECKING U {} V {}".format(u, v))
            if u in visited:
                print("U IN VISITED {}".format(str(visited)))
                return False
            if u == v:
                return True

            visited.add(u)

            print("U {} CONNECTED TO {}".format(u, str(graph[u])))
            for neighbor in graph[u]:
                print("CALLSTACK NEIGHBOR {}  NODE {}".format(neighbor, v))
                if dfs(neighbor, v):
                    return True
            return False

        graph = collections.defaultdict(list)

        ans = []

        for u, v in edges:
            print("\n**** ADDING {} {}".format(u, v))
            visited = set()
            if dfs(u, v):
                ans = [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return ans

    def test_rc(self):
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        self.assertEqual(self.find_redundant_connection(edges), [1,4])


# LOGGING
# **** ADDING 1 2
# CHECKING U 1 V 2
#      U 1 CONNECTED TO []
#
# **** ADDING 2 3
# CHECKING U 2 V 3
#      U 2 CONNECTED TO [1]
# CALLSTACK NEIGHBOR 1  NODE 3
# CHECKING U 1 V 3
#      U 1 CONNECTED TO [2]
# CALLSTACK NEIGHBOR 2  NODE 3
# CHECKING U 2 V 3
# U IN VISITED {1, 2}
#
# **** ADDING 3 4
# CHECKING U 3 V 4
#      U 3 CONNECTED TO [2]
# CALLSTACK NEIGHBOR 2  NODE 4
# CHECKING U 2 V 4
#      U 2 CONNECTED TO [1, 3]
# CALLSTACK NEIGHBOR 1  NODE 4
# CHECKING U 1 V 4
#      U 1 CONNECTED TO [2]
# CALLSTACK NEIGHBOR 2  NODE 4
# CHECKING U 2 V 4
# U IN VISITED {1, 2, 3}
# CALLSTACK NEIGHBOR 3  NODE 4
# CHECKING U 3 V 4
# U IN VISITED {1, 2, 3}
#
# **** ADDING 1 4
# CHECKING U 1 V 4
#      U 1 CONNECTED TO [2]
# CALLSTACK NEIGHBOR 2  NODE 4
# CHECKING U 2 V 4
#      U 2 CONNECTED TO [1, 3]
# CALLSTACK NEIGHBOR 1  NODE 4
# CHECKING U 1 V 4
# U IN VISITED {1, 2}
# CALLSTACK NEIGHBOR 3  NODE 4
# CHECKING U 3 V 4
#      U 3 CONNECTED TO [2, 4]
# CALLSTACK NEIGHBOR 2  NODE 4
# CHECKING U 2 V 4
# U IN VISITED {1, 2, 3}
# CALLSTACK NEIGHBOR 4  NODE 4
# CHECKING U 4 V 4
# ANS [1, 4]
#
# **** ADDING 1 5
# CHECKING U 1 V 5
#      U 1 CONNECTED TO [2, 4]
# CALLSTACK NEIGHBOR 2  NODE 5
# CHECKING U 2 V 5
#      U 2 CONNECTED TO [1, 3]
# CALLSTACK NEIGHBOR 1  NODE 5
# CHECKING U 1 V 5
# U IN VISITED {1, 2}
# CALLSTACK NEIGHBOR 3  NODE 5
# CHECKING U 3 V 5
#      U 3 CONNECTED TO [2, 4]
# CALLSTACK NEIGHBOR 2  NODE 5
# CHECKING U 2 V 5
# U IN VISITED {1, 2, 3}
# CALLSTACK NEIGHBOR 4  NODE 5
# CHECKING U 4 V 5
#      U 4 CONNECTED TO [3, 1]
# CALLSTACK NEIGHBOR 3  NODE 5
# CHECKING U 3 V 5
# U IN VISITED {1, 2, 3, 4}
# CALLSTACK NEIGHBOR 1  NODE 5
# CHECKING U 1 V 5
# U IN VISITED {1, 2, 3, 4}
# CALLSTACK NEIGHBOR 4  NODE 5
# CHECKING U 4 V 5
# U IN VISITED {1, 2, 3, 4}