import unittest

class IsomorphicStrings(unittest.TestCase):
    """
    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat process until number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    """
    def isomorphic_strings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
        # alternate solution using sets and zip function
        # zipped_set = set(zip(s, t))
        # return len(zipped_set) == len(set(s)) == len(set(t))

    def test_isomorphic_strings(self):
        self.assertTrue(self.isomorphic_strings('eggs', 'adds'))
        self.assertFalse(self.isomorphic_strings('legs', 'been'))



