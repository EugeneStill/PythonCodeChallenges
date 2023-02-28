import unittest
import collections
import helpers.binary_tree as binary_tree


class RightSideView(unittest.TestCase):
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.
    """
    def right_side_view(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        deque = collections.deque()
        if root:
            deque.append(root)
        res = []
        while deque:
            size, val = len(deque), 0
            for _ in range(size):
                node = deque.popleft()
                val = node.val # store last value in each level
                # even though we are looking at right side view, a child level might only have a left node so check both
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(val)
        return res

    def test_rsv(self):
        level_input = [1, 2, 3, None, 5, None, 4]
        output = [1, 3, 4]
        bt = binary_tree.BST()
        bt.build_binary_tree(level_input)
        self.assertEqual(self.right_side_view(bt.root), output)