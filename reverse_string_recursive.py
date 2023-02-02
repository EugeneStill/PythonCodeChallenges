import unittest


class ReverseString(unittest.TestCase):
    """
    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.
    """
    def reverse_string(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1

        def recursive_reverse(s, index):
            if index < len(s) / 2:
                s[index], s[end - index] = s[end - index], s[index]
                index = index + 1
                recursive_reverse(s, index)
            else:
                return
        recursive_reverse(s, 0)
        return s

    def test_rev_string(self):
        self.assertEqual(self.reverse_string(["E", "u", "g", "e", "n", "e"]), ["e", "n", "e", "g", "u", "E"])

