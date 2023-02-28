import unittest
import helpers.binary_tree as binary_tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec():
    """
    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
    stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
    in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree.
    There is no restriction on how your serialization/deserialization algorithm should work.
    You just need to ensure that a binary tree can be serialized to a string and this string can be
    deserialized to the original tree structure.

    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]
    """
    def serialize(self, root):
        def build_list(node):
            if node:
                vals.append(str(node.val))
                build_list(node.left)
                build_list(node.right)
            else:
                vals.append('#')
        vals = []
        build_list(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def build_tree(side):
            val = next(vals)
            print("PARSING {} FOR {} SIDE".format(val, side))
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build_tree("LEFT")
            node.right = build_tree("RIGHT")
            return node
        vals = iter(data.split())
        return build_tree("ROOT")


class TestSerDer(unittest.TestCase):
    def get_tree_list(self, tree_node, order="preorder"):
        def parse_tree(tree_node, order):
            if order == "preorder":
                list_output.append(tree_node.val)
            if tree_node.left is not None:
                parse_tree(tree_node.left, order)
            if order == "inorder":
                list_output.append(tree_node.val)
            if tree_node.right is not None:
                parse_tree(tree_node.right, order)
            if order == "postorder":
                list_output.append(tree_node.val)
        list_output = []
        parse_tree(tree_node, order)
        return list_output

    def test_ser_der(self):
        root = [1,2,3,None,None,4,5]
        bt = binary_tree.BST()
        bt.build_binary_tree(root)
        ser = Codec()
        deser = Codec()
        ans = deser.deserialize(ser.serialize(bt.root))
        self.assertEqual(self.get_tree_list(ans), self.get_tree_list(bt.root))