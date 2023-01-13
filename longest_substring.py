import unittest

class LongSub(unittest.TestCase):

    def longest_sub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        count, s_result = 0, ''

        for i in s:
            if i not in s_result:
                s_result += i
            else:
                # add current char to substring of s_result after removing first occurrence of that char from s_result
                s_result = s_result[s_result.index(i) + 1:] + i
            if len(s_result) >= count:
                count = len(s_result)
        return count

    def test_lwl(self):
        self.assertEqual(self.longest_sub('dvdf'), 3)



