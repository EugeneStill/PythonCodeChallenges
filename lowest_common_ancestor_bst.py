import unittest
import helpers.binary_tree as binary_tree


class LowestCommonAncestor(unittest.TestCase):
    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as
    descendants (where we allow a node to be a descendant of itself).”

    We will rely upon the invariant of the BST to solve the exercise. We know that the left subtree of each node
    contains nodes with smaller values and the right subtree contains nodes with greater values.
    We also know that if two nodes, x and y, are on different subtrees of a node z
    (one in the left portion and one in the right portion), then x and y have z as the lowest common ancestor.
    """
    def lowest_common_ancestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: TreeNode
        """
        while root:
            if root.val > p and root.val > q:
                root = root.left
            elif root.val < p and root.val < q:
                root = root.right
            else:
                return root

    def test_lca(self):
        bst = binary_tree.BST()
        bst.insert_level([6,2,8,0,4,7,9,None,None,3,5], 0, 11)
        self.assertEqual(self.lowest_common_ancestor(bst.root, 2, 8).val, 6)