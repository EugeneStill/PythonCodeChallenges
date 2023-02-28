import unittest
import collections


class FindMinHeightTrees(unittest.TestCase):
    """
    A tree is an undirected graph in which any two vertices are connected by exactly one path.
    In other words, any connected graph without simple cycles is a tree.

    Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi]
    indicates that there is an undirected edge between the two nodes ai and bi in the tree,
    you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h.
    Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

    Return a list of all MHTs' root labels. You can return the answer in any order.

    The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

    Input: n = 4, edges = [[1,0],[1,2],[1,3]]
    Output: [1]
    Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.


    HINT
    We can find the leaf nodes at each iteration using the indegree of the node, i.e,
    the number of edges which are connected to the node.
    A leaf node will have an indegree of 1.
    The algorithm used will be similar to BFS.
    At each level of BFS, we will pop the leaf node and push the new nodes
    which become leaves after deletion of leaf nodes in the current iteration.
    This will continue till we are left with only 1 or 2 nodes which would be our final mid-nodes forming the MHTs.
    """
    def find_mht(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        total_node_count = n

        if total_node_count == 1:
            return [0]

        # build adjacency matrix
        adj_matrix = collections.defaultdict(set)

        for src_node, dst_node in edges:
            adj_matrix[src_node].add(dst_node)
            adj_matrix[dst_node].add(src_node)

        # get leaves node whose degree is 1
        leave_nodes = [node for node in adj_matrix if len(adj_matrix[node]) == 1]

        # keep doing leave nodes removal until total node count is smaller or equal to 2
        # If there are only two nodes left, then they will both be considered as leaves which will be removed.
        # If there are three nodes left, then two of them will be leaves and one will be the node we need.
        while total_node_count > 2:


            total_node_count -= len(leave_nodes)
            print("\nSTART LEAVE NODES {} TOTAL NODES {}".format(str(leave_nodes), total_node_count))

            leave_nodes_next_round = []

            # leave nodes removal
            for leaf in leave_nodes:
                print("GETTING LEAF's ONLY NEIGHBOR {}".format(leaf))
                neighbor = adj_matrix[leaf].pop()
                print("REMOVING LEAF {} FROM {}'s LIST OF NEIGHBORS".format(leaf, neighbor))
                adj_matrix[neighbor].remove(leaf)


                if len(adj_matrix[neighbor]) == 1:
                    leave_nodes_next_round.append(neighbor)
                    print("{} ONLY HAS ONE NEIGHBOR. ADDING TO NEXT ROUND".format(neighbor))
                else:
                    print("{} HAS {} NEIGHBORS".format(neighbor, len(adj_matrix[neighbor])))

            leave_nodes = leave_nodes_next_round
            print("\nEND LEAVE NODES {} TOTAL NODES {}".format(str(leave_nodes), total_node_count))

        # final leave nodes are root node of minimum height trees
        return leave_nodes


    def test_mht(self):
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        self.assertEqual(self.find_mht(n, edges), [1])
        n = 6
        edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
        Output: [3, 4]
        self.assertEqual(self.find_mht(n, edges), [3, 4])


# LOGGING
# START LEAVE NODES [0, 2, 3] TOTAL NODES 1
# CHECKING LEAF 0
# REMOVING LEAF 0 FROM NEIGHBOR 1
# 1 HAS 2 NEIGHBORS
# CHECKING LEAF 2
# REMOVING LEAF 2 FROM NEIGHBOR 1
# 1 ONLY HAS ONE NEIGHBOR. ADDING TO NEXT ROUND
# CHECKING LEAF 3
# REMOVING LEAF 3 FROM NEIGHBOR 1
# 1 HAS 0 NEIGHBORS
#
# END LEAVE NODES [1] TOTAL NODES 1
#
# START LEAVE NODES [0, 1, 2, 5] TOTAL NODES 2
# CHECKING LEAF 0
# REMOVING LEAF 0 FROM NEIGHBOR 3
# 3 HAS 3 NEIGHBORS
# CHECKING LEAF 1
# REMOVING LEAF 1 FROM NEIGHBOR 3
# 3 HAS 2 NEIGHBORS
# CHECKING LEAF 2
# REMOVING LEAF 2 FROM NEIGHBOR 3
# 3 ONLY HAS ONE NEIGHBOR. ADDING TO NEXT ROUND
# CHECKING LEAF 5
# REMOVING LEAF 5 FROM NEIGHBOR 4
# 4 ONLY HAS ONE NEIGHBOR. ADDING TO NEXT ROUND
#
# END LEAVE NODES [3, 4] TOTAL NODES 2