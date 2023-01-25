import unittest

class FourSumII(unittest.TestCase):
    """
    Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
    """

    def four_sumII(self, A, B, C, D):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        dic = {}
        for a in A:
            for b in B:
                if a + b in dic:
                    dic[a + b] += 1
                else:
                    dic[a + b] = 1
        count = 0
        for c in C:
            for d in D:
                if -c - d in dic:
                    count += dic[-c - d]
        return count

    def test_fsII(self):
        A = [1, 2]
        B = [-2, -1]
        C = [-1, 2]
        D = [0, 2]
        self.assertEqual(self.four_sumII(A,B,C,D), 2)



