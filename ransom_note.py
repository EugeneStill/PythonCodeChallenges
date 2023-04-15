import unittest
from collections import defaultdict

class RansomNote(unittest.TestCase):
    def can_construct(self, ransom_note, magazine):
        """
        :type ransom_note: str
        :type magazine: str
        :rtype: bool
        """
        magazine_chars = defaultdict(int)
        for c in magazine:
            magazine_chars[c] += 1

        for c in ransom_note:
            if c not in magazine_chars or magazine_chars[c] == 0:
                return False
            magazine_chars[c] -= 1
        return True

    def test_ransom_note(self):
        self.assertTrue(self.can_construct("send money now", "wow my honey ends soon"))
        self.assertFalse(self.can_construct("send cash now", "wow my honey ends soon"))
