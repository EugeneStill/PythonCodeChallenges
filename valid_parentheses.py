import unittest

class TestChallenge(unittest.TestCase):

    def is_valid_p(self, s: str) -> bool:
        stack = []

        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in mapping.keys():
                stack.append(mapping[char])
            elif not stack or stack[-1] != char:
                return False
            else:
                stack.pop()

        return len(stack) == 0

    def test_vp(self):
        self.assertTrue(self.is_valid_p('()[]{}'))
        self.assertFalse(self.is_valid_p('[}]'))


