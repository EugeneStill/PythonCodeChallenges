import unittest

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class SymmetricTree(unittest.TestCase):
    def is_symmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not (l and r) or l.val != r.val:
                return False
            stack.extend([(l.left, r.right), (l.right, r.left)])
        return True

