import unittest
import helpers.binary_tree as binary_tree

class DiameterOfBinaryTree(unittest.TestCase):
    """
    Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.
    """
    def diameter_of_binary_tree(self, root):
        result = [0]  # Global result variable
        self.find_diameter(root, result)
        return result[0]

    def find_diameter(self, root, result):
        if not root:
            return 0

        left = self.find_diameter(root.left, result)
        right = self.find_diameter(root.right, result)

        result[0] = max(result[0], left + right)

        return max(left, right) + 1

    def test_diameter(self):
        bt = binary_tree.BST()
        bt.build_binary_tree([1,2,3,4,5])
        self.assertEqual(self.diameter_of_binary_tree(bt.root), 3)