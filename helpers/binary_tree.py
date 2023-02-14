# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.root = None

class BST(object):
    def __init__(self):
        self.root = None
        self.list_output = []

    # build out a tree
    def insert_level(self, arr, i, n):
        root = None
        # Base case for recursion
        if i < n:
            root = TreeNode(arr[i])
            if self.root is None:
                self.root = root
            # insert left child
            root.left = self.insert_level(arr, 2 * i + 1, n)
            # insert right child
            root.right = self.insert_level(arr, 2 * i + 2, n)
        return root

    def build_binary_tree(self, level_order):
        values = iter(level_order)
        root = TreeNode(next(values))
        nodes_to_fill = [root]
        try:
            while True:
                next_node = nodes_to_fill.pop(0)
                new_left = next(values)
                if new_left is not None:
                    next_node.left = TreeNode(new_left)
                    nodes_to_fill.append(next_node.left)
                new_right = next(values)
                if new_right is not None:
                    next_node.right = TreeNode(new_right)
                    nodes_to_fill.append(next_node.right)
        except StopIteration:
            self.root = root

    def print_tree(self, tree_node, order="preorder"):
        if order == "preorder":
            print(tree_node.val)
            self.list_output.append(tree_node.val)
        if tree_node.left is not None:
            self.print_tree(tree_node.left)
        if order == "inorder":
            print(tree_node.val)
            self.list_output.append(tree_node.val)
        if tree_node.right is not None:
            self.print_tree(tree_node.right)
        if order == "postorder":
            print(tree_node.val)
            self.list_output.append(tree_node.val)
        return self.list_output