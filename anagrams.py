import unittest
import collections


class Anagrams(unittest.TestCase):
    """
    Given two strings s and t (with only lowercase letters), return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    """
    def is_anagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic_s = collections.defaultdict(int)
        dic_t = collections.defaultdict(int)

        for i in range(len(s)):
            dic_s[s[i]] += 1
            dic_t[t[i]] += 1

        return dic_s == dic_t

    def test_anagram(self):
        self.assertTrue(self.is_anagram("racecar", "carrace"))
        self.assertFalse(self.is_anagram("facecar", "carrace"))