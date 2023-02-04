import unittest


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
        dic1 = {}
        dic2 = {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

    def test_anagram(self):
        self.assertTrue(self.is_anagram("racecar", "carrace"))
        self.assertFalse(self.is_anagram("facecar", "carrace"))