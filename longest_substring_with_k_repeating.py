import unittest


class LSK(unittest.TestCase):
    """
    Given a string s and an integer k, return the length of the longest substring of s
    such that the frequency of each character in this substring is greater than or equal to k.
    """

    def longest_sub_k_repeating(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longest_sub_k_repeating(t, k) for t in s.split(c))
        # this is only invoked when all characters in s are >= k, so the whole string is used
        return len(s)

    def test_longest_sub_k(self):
        s = "ababbc"
        k = 2
        ans = 5
        self.assertEqual(self.longest_sub_k_repeating(s, k), ans)
