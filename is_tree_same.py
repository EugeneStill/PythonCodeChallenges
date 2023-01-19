import unittest
import helpers.binary_tree as binary_tree

class IsTreeSame(unittest.TestCase):
    def is_tree_same(self, p, q):
        # base case: both nodes are null
        if not p and not q:
            return True
        # base case: one node is null
        if not p or not q:
            return False
        # check if the values of the nodes are the same
        if p.val != q.val:
            return False
        # check if the left and right subtrees are the same
        return self.is_tree_same(p.left, q.left) and self.is_tree_same(p.right, q.right)

    def test_is_tree_same(self):
        bt = binary_tree.TreeNode()
        tree_123 = bt.insert_level([1, 2, 3], 0, 3)
        tree_321 = bt.insert_level([3, 2, 1], 0, 3)
        self.assertTrue(self.is_tree_same(tree_123, tree_123))
        self.assertFalse(self.is_tree_same(tree_321, tree_123))



