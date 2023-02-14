import unittest
import helpers.binary_tree as binary_tree


class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LowestCommonAncestor(unittest.TestCase):
    """
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
    as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    # DEBUG LOCALLY.  WORKS ON LEETCODE BUT NOT LOCALLY.
    """
    def lowest_common_ancestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: TreeNode
        """
        print("ROOT {}".format(root.val))
        if root == p or root == q:
            return root

        left = right = None

        if root.left:
            left = self.lowest_common_ancestor(root.left, p, q)
        if root.right:
            right = self.lowest_common_ancestor(root.right, p, q)

        # if both children returned a node, means both p and q found so parent is LCA
        if left and right:
            print("GOT LEFT & RIGHT")
            return root
        elif left or right:
            # only one of the chidren returned a node, meaning either p or q found on left or right branch.
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way,
            # because in such scenarios, node where 'p' found is LCA
            print("ONLY GOT LEFT OR RIGHT")
            print("L {} R {}".format(left, right))
            return left or right
        else:
            print("NO NODES FOUND")


    def test_lca(self):
        bt = binary_tree.BST()
        bt.build_binary_tree([3,5,1,6,2,0,8,None,None,7,4])
        self.assertEqual(self.lowest_common_ancestor(bt.root, 5, 1), 3)