import unittest

import helpers.binary_tree as binary_tree


class MaxDepth(unittest.TestCase):
    def bst_max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)

    def test_search(self):
        bt = binary_tree.BST()
        bt.insert_level([3,9,20,None,None,15,7], 0, 7)
        # res = self.bst_max_depth(bt.root, 2)
        self.assertEqual(self.bst_max_depth(bt.root), 3)
