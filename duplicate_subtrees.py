import unittest
import collections
import helpers.binary_tree as binary_tree

class FindDuplicateSubtrees(unittest.TestCase):
    def find_duplicate_sub_trees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        def trv(root):
            if not root:
                return None
            sub_tree = "{},{},{}".format(str(root.val), trv(root.left), trv(root.right))
            nodes[sub_tree].append(root)
            return sub_tree

        nodes = collections.defaultdict(list)
        trv(root)
        return [nodes[sub_tree][0] for sub_tree in nodes if len(nodes[sub_tree]) > 1]

    def test_is_tree_bst(self):
        bt = binary_tree.TreeNode()
        tree1 = bt.insert_level([1,2,3,4,None,2,4,None,None,4], 0, 10)
        res = self.find_duplicate_sub_trees(tree1)
        for r in res:
            print(r.val, r.left, r.right)



