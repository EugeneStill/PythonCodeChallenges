import unittest


class ReverseBits(unittest.TestCase):

    def reverse_bits(self, n):
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        print(out)
        return out

    def test_reverse_bits(self):
        n = 0b00000010100101000001111010011100
        result = 0b00111001011110000010100101000000
        # 964176192
        self.assertEqual(self.reverse_bits(n), result)