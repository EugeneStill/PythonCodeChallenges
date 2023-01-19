import unittest
import helpers.binary_tree as binary_tree

class IsTreeBst(unittest.TestCase):
    def check_bst(self, root):
        return self.check(root, -1, 100000)

    def check(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.check(root.left, min, root.val) and self.check(root.right, root.val, max)

    def test_is_tree_bst(self):
        bt = binary_tree.TreeNode()
        tree_123 = bt.insert_level([2, 1, 3], 0, 3)
        tree_321 = bt.insert_level([3, 2, 1], 0, 3)
        self.assertTrue(self.check_bst(tree_123))
        self.assertFalse(self.check_bst(tree_321))



