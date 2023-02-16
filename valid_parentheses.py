import unittest

class TestChallenge(unittest.TestCase):

    def is_valid_p(self, s: str) -> bool:
        stack = [0]
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if mapping[stack.pop()] != c:
                    return False
        return stack == [0]

    def test_vp(self):
        self.assertTrue(self.is_valid_p('()[]{}'))
        self.assertFalse(self.is_valid_p('[}]'))


