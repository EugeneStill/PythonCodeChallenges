import unittest

class TopKFrequentElements(unittest.TestCase):
    """
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    """

    def k_frequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        sorted_keys = [num for num, count in sorted(dic.items(), key=lambda x: x[1], reverse=True)]
        return sorted_keys[:k]

    def test_k_frequent(self):
        self.assertEqual(self.k_frequent([1,1,1,2,2,3], 2), [1,2])



