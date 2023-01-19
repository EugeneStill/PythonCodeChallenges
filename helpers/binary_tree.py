# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # build out a tree
    def insert_level(self, arr, i, n):
        root = None
        # Base case for recursion
        if i < n:
            root = TreeNode(arr[i])
            # insert left child
            root.left = self.insert_level(arr, 2 * i + 1, n)
            # insert right child
            root.right = self.insert_level(arr, 2 * i + 2, n)
        return root
