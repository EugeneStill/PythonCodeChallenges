import unittest


class AddBinary(unittest.TestCase):
    """
    Given two binary strings a and b, return their sum as a binary string.
    https://www.cuemath.com/numbers/binary-addition/ 
    """
    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        rem, res, a, b = 0, "", list(a), list(b)

        while a or b:
            if a:
                rem += int(a.pop())
            if b:
                rem += int(b.pop())
            res = str(rem % 2) + res
            rem = rem // 2
        if rem == 1:
            res = str(rem) + res
        return res

    def test_binary_add(self):
        a, b = "1010", "1011"
        self.assertEqual(self.add_binary(a, b), "10101")
        a, b = "11", "1"
        self.assertEqual(self.add_binary(a, b), "100")

