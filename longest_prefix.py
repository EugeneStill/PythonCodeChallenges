import unittest

class LongestPrefix(unittest.TestCase):

    def lcp(self, strs) -> str:
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

    def test_lcp(self):
        self.assertEqual(self.lcp(['car', 'car crash', 'car race']), 'car')



