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
        rem, res = 0, ""
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or rem > 0:
            if i >= 0:
                rem += int(a[i])
                i -= 1
            if j >= 0:
                rem += int(b[j])
                j -= 1
            res = str(rem % 2) + res
            rem = rem // 2
        return res

    def test_binary_add(self):
        a, b = "1010", "1011"
        self.assertEqual(self.add_binary(a, b), "10101")
        a, b = "11", "1"
        self.assertEqual(self.add_binary(a, b), "100")

