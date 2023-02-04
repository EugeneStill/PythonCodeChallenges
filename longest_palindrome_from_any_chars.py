import unittest
import collections


class LongestPalindrome(unittest.TestCase):
    """
    Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that
    can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
    """
    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = set()
        offset = 0
        for c in s:
            if c not in odds:
                odds.add(c)
            else:
                odds.remove(c)
        if len(odds) > 0:
            offset = 1
        return len(s) - len(odds) + offset

    def test_lp(self):
        self.assertEqual(self.longest_palindrome("aaaccc"), 5)