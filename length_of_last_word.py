import unittest

class LastWordLen(unittest.TestCase):

    def lwl(self, s):
        """
        :type s: str
        :rtype: str
        """
        return len(s.split()[-1].strip())

    def test_lwl(self):
        self.assertEqual(self.lwl('a'), 1)



