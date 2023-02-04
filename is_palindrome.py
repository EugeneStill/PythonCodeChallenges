import unittest


class IsPalindrome(unittest.TestCase):
    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -= 1
        return True

    def test_pal(self):
        self.assertTrue(self.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.is_palindrome("race a car"))