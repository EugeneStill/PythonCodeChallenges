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
        self.best = 0
        def depth(root):
            if not root:
                return 0
            ans_left = depth(root.left)
            ans_right = depth(root.right)
            self.best = max(self.best, ans_left + ans_right)
            return 1 + max(ans_left, ans_right)
        depth(root)
        return self.best

    def test_diameter(self):
        bt = binary_tree.BST()
        bt.build_binary_tree([1,2,3,4,5])
        self.assertEqual(self.diameter_of_binary_tree(bt.root), 3)