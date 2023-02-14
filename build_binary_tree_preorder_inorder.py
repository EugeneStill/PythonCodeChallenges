import unittest
import helpers.binary_tree as binary_tree

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class ConstructTree(unittest.TestCase):
    """
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder
    is the inorder traversal of the same tree, construct and return the binary tree.

    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
    """
    def construct_tree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            # get root preorder[0] then find index of that value in inorder
            idx = inorder.index(preorder.pop(0))
            root = binary_tree.TreeNode(inorder[idx])
            # use left side of idx to build left side of tree and right side of idx to build right side of tree
            root.left = self.construct_tree(preorder, inorder[0:idx])
            root.right = self.construct_tree(preorder, inorder[idx+1:])
            return root

    def test_construction(self):
        bt = binary_tree.BST()
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        output = [3, 9, 20, 15, 7]
        self.assertEqual(bt.print_tree(self.construct_tree(preorder, inorder)), output)
        # bt.print_tree(new_tree)
