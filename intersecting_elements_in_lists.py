import unittest

class IntersectingElements(unittest.TestCase):
    """
    return index of first unique character in a string, else return -1
    """

    def get_intersecting_elements(self, l1, l2):
        """
        :type l1: list
        :type l2: list
        :rtype: list
        """
        dic = {}
        res = []
        for c in l1:
            dic[c] = dic.get(c,0) + 1
        for c in l2:
            if dic.get(c, 0) > 0:
                res.append(c)
                dic[c] -= 1
        return res

    def test_intersecting_elements(self):
        l1 = [1, 1, 2, 3, 4, 5, 6]
        l2 = [1, 3, 1, 6]
        l3 = [5]
        l4 = [19]
        self.assertEqual(self.get_intersecting_elements(l1, l2), [1, 3, 1, 6])
        self.assertEqual(self.get_intersecting_elements(l1, l3), [5])
        self.assertEqual(self.get_intersecting_elements(l3, l4), [])



