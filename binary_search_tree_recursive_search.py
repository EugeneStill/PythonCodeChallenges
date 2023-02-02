import unittest

import helpers.binary_tree as binary_tree


class SearchBST(unittest.TestCase):
    def search_bst(self, root, val):  # recursively
        if not root or root.val == val:
            return root
        elif root.val > val:
            return self.search_bst(root.left, val)
        else:
            return self.search_bst(root.right, val)

    def test_search(self):
        bt = binary_tree.BST()
        bt.insert_level([4,2,7,1,3], 0, 5)
        res = self.search_bst(bt.root, 2)
        self.assertEqual([res.val, res.left.val, res.right.val], [2,1,3])
