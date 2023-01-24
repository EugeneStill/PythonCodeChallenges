import unittest

class MinIdxSum2Lists(unittest.TestCase):
    """
    Given two arrays of strings list1 and list2, find the common strings with the least index sum.
    Return all the common strings with the least index sum. Return the answer in any order.

    1 <= list1.length, list2.length <= 1000
    1 <= list1[i].length, list2[i].length <= 30
    list1[i] and list2[i] consist of spaces ' ' and English letters.
    All the strings of list1 are unique.
    All the strings of list2 are unique.

    Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
    Output: ["Shogun"]
    Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

    Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
    Output: ["sad","happy"]
    Explanation: There are three common strings:
    "happy" with index sum = (0 + 1) = 1.
    "sad" with index sum = (1 + 0) = 1.
    "good" with index sum = (2 + 2) = 4.
    The strings with the least index sum are "sad" and "happy".
    """
    def min_idx_sum(self, l1, l2):
        """
        :type l1: list
        :type l2: list
        :rtype: list
        """
        dic1 = {s: i for i, s in enumerate(l1)}
        dic2 = {s: dic1[s] + i for i, s in enumerate(l2) if s in dic1}

        least = float('inf')
        res = []

        for s, v in dic2.items():
            if v < least:
                res = [s]
                least = v
            elif v == least:
                res.append(s)

        return res

    def test_isomorphic_strings(self):
        l1 = ["happy","sad","good"]
        l2 = ["sad","happy","good"]
        l3 = ["Barney's", "Cactus", "Delhi Diner"]
        l4 = ["Delhi Diner"]
        res1 = self.min_idx_sum(l1, l2)
        self.assertTrue(len(res1) == 2 and l1[0] in res1 and l1[1] in res1)
        self.assertEqual(self.min_idx_sum(l3, l4), l4)



