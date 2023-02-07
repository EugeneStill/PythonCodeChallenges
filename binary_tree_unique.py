import unittest

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class GenerateTrees(unittest.TestCase):
    """
    Given an integer n, return all the structurally unique BST's (binary search trees),
    which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
    ***** DO DEEPER DIVE ON THIS ONE *********
    """
    def generate_trees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        cache = {}
        def generate(first, last):
            if first > last:
                print("FIRST {} > LAST {}".format(first, last))
                return [None]
            if (first, last) in cache:
                print("GOT {} {} FROM CACHE".format(first, last))
                return cache[first, last]
            trees = []
            for root in range(first, last+1):
                print("\nMADE LEFT CALL FOR ROOT {}".format(first))
                for left in generate(first, root-1):
                    print("\nMAKING RIGHT CALL FOR ROOT + 1 {}".format(root+1))
                    for right in generate(root+1, last):
                        print("\nCREATING NODE ROOT {}, LEFT {}, RIGHT {}".format(root, left, right))
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            cache[first, last] = trees
            return trees
        return generate(1, n)


    def test_unique_trees(self):
        """
        Input: n = 3
        Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
        """
        print(str(self.generate_trees(3)))