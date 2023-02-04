import unittest
import collections
import helpers.binary_tree as binary_tree


class InvertTree(unittest.TestCase):
    """
    Given the root of a binary tree, invert the tree, and return its root.
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    """
    def invert_tree_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root

    def invert_tree_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        q = collections.deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return root

    def invert_tree_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left

            if root.left:
                self.invert_tree_recursion(root.left)
            if root.right:
                self.invert_tree_recursion(root.right)
            return root
        else:
            return None

    def test_inversion(self):
        input = [4,2,7,1,3,6,9]
        bt1 = binary_tree.BST()
        bt2 = binary_tree.BST()
        bt3 = binary_tree.BST()
        bt1.insert_level(input, 0, 7)
        bt2.insert_level(input, 0, 7)
        bt3.insert_level(input, 0, 7)
        self.invert_tree_recursion(bt1.root)
        self.invert_tree_bfs(bt2.root)
        self.invert_tree_bfs(bt3.root)
        self.assertEqual(bt1.root.left.left.val, 9)
