import unittest


class RansomNote(unittest.TestCase):
    def can_construct(self, ransom_note, magazine):
        """
        :type ransom_note: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransom_note):
            if ransom_note.count(i) > magazine.count(i):
                return False
        return True

    def test_ransom_note(self):
        self.assertTrue(self.can_construct("send money now", "wow my honey ends soon"))
        self.assertFalse(self.can_construct("send cash now", "wow my honey ends soon"))
