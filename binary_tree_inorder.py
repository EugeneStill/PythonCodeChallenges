import unittest
import helpers.binary_tree as binary_tree

class BinaryTreeInorder(unittest.TestCase):
    """
    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    """

    def inorder_traversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                print("ADDED {} TO STACK".format(root.val))
                root = root.left
            if not stack:
                print(str(res))
                return res
            node = stack.pop()
            res.append(node.val)
            print("POPPED {} FROM STACK & ADDED TO RES".format(node.val))
            root = node.right

    def test_inorder(self):
        bt = binary_tree.TreeNode()
        tree1 = bt.insert_level([1, None, 2, 3, None], 0, 5)
        self.assertEqual(self.inorder_traversal(tree1), [1,3,2])



