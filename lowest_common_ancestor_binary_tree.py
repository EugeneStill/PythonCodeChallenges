import unittest
import helpers.binary_tree as binary_tree


class LowestCommonAncestor(unittest.TestCase):
    """
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
    as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    """
    def lowest_common_ancestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: TreeNode
        """
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
        else:
            # only one of the chidren returned a node, meaning either p or q found on left or right branch.
            # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
            # somewhere below node where 'p' was found we dont need to search all the way,
            # because in such scenarios, node where 'p' found is LCA
            print("ONLY GOT LEFT OR RIGHT")
            print("L {} R {}".format(left, right))
            return left or right

    def test_lca(self):
        bst = binary_tree.BST()
        bst.insert_level([3,5,1,6,2,0,8,None,None,7,4], 0, 11)
        print(bst.root.left.val)
        self.assertEqual(self.lowest_common_ancestor(bst.root, 5, 1).val, 3)