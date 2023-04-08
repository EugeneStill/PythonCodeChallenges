import unittest


class Solution(unittest.TestCase):
    """
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
    """
    def substring_search(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1

    def test_substring_search(self):
        self.assertEqual(self.substring_search("haystack", "needle"), -1)
        self.assertEqual(self.substring_search("haystack", "stack"), 3)
