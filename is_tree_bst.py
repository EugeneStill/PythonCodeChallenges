import unittest
import helpers.binary_tree as binary_tree

class IsTreeBst(unittest.TestCase):
    def check_bst(self, root):
        def check(root, min_val, max_val):
            if not root:
                return True
            if not min_val < root.val < max_val:
                return False
            return check(root.left, min_val, root.val) and check(root.right, root.val, max_val)

        return check(root, -float("inf"), float("inf"))

    def test_is_tree_bst(self):
        bt = binary_tree.BST()
        tree_123 = bt.insert_level([2, 1, 3], 0, 3)
        tree_321 = bt.insert_level([3, 2, 1], 0, 3)
        self.assertTrue(self.check_bst(tree_123))
        self.assertFalse(self.check_bst(tree_321))



