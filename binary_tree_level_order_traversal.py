import unittest
from collections import deque
import helpers.binary_tree as binary_tree



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class LevelOrder(unittest.TestCase):
    def level_order(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        queue, res = deque([root]), []

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res

    def test_lo(self):
        bt = binary_tree.BST()
        bt.insert_level([3,9,20,None,None,15,7], 0, 7)
        self.assertEqual(self.level_order(bt.root), [[3],[9,20],[None, None, 15,7]])
