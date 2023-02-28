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

        # put root inside a list since we instantiate deque using an iterable
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
        print("\n")
        if root:
            root.left, root.right = root.right, root.left

            # while there are root children, recurse left/right (if they exist)
            if root.left:
                print("FOR ROOT {} RECURSING LEFT".format(root.val))
                self.invert_tree_recursion(root.left)
            if root.right:
                print("FOR ROOT {} RECURSING RIGHT".format(root.val))
                self.invert_tree_recursion(root.right)
            print("RETURNING ROOT {}".format(root.val))
            return root
        else:
            return None

    def test_inversion(self):
        input_list = [4,2,7,1,3,6,9]
        bt1 = binary_tree.BST()
        bt2 = binary_tree.BST()
        bt3 = binary_tree.BST()
        bt1.insert_level(input_list, 0, 7)
        bt2.insert_level(input_list, 0, 7)
        bt3.insert_level(input_list, 0, 7)
        self.invert_tree_recursion(bt1.root)
        self.invert_tree_bfs(bt2.root)
        self.invert_tree_bfs(bt3.root)
        self.assertEqual(bt1.root.left.left.val, 9)

# RECURSION LOGGING
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
# FOR ROOT 4 RECURSING LEFT
#
# FOR ROOT 7 RECURSING LEFT
#
# RETURNING ROOT 9
# FOR ROOT 7 RECURSING RIGHT
#
# RETURNING ROOT 6
# RETURNING ROOT 7
# FOR ROOT 4 RECURSING RIGHT
#
# FOR ROOT 2 RECURSING LEFT
#
# RETURNING ROOT 3
# FOR ROOT 2 RECURSING RIGHT
#
# RETURNING ROOT 1
# RETURNING ROOT 2
# RETURNING ROOT 4