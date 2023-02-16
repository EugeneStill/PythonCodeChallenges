import unittest

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class IsBalanced(unittest.TestCase):
    """
    A height-balanced binary tree is a binary tree where the difference in depth of the 2 subtrees never > 1
    """
    # def is_balanced(self, root):
    #     self.Bal = True
    #     self.dfs(root)
    #     return self.Bal
    #
    # def dfs(self, node):
    #      if not node: return 0
    #      lft, rgh = self.dfs(node.left), self.dfs(node.right)
    #      if abs(lft - rgh) > 1:
    #          self.Bal = False
    #      return max(lft, rgh) + 1
    def is_balanced(self, root):
        return (self.height(root) >= 0)

    def height(self, root):
        if root is None:
            return 0
        leftheight, rightheight = self.height(root.left), self.height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1

    def binary_tree(self, level_order):
        values = iter(level_order)
        root = Node(next(values))
        nodes_to_fill = [root]
        try:
            while True:
                next_node = nodes_to_fill.pop(0)
                new_left = next(values)
                if new_left is not None:
                    next_node.left = Node(new_left)
                    nodes_to_fill.append(next_node.left)
                new_right = next(values)
                if new_right is not None:
                    next_node.right = Node(new_right)
                    nodes_to_fill.append(next_node.right)
        except StopIteration:
            return root

    def test_bt(self):
        bt1 = self.binary_tree([3,9,20,None,None,15,7])
        self.assertTrue(self.is_balanced(bt1))
        bt2 = self.binary_tree([1,2,2,3,3,None,None,4,4])
        self.assertFalse(self.is_balanced(bt2))