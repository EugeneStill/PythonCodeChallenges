import unittest


class OneBits(unittest.TestCase):
    """
    return number of 1 bits in number
    """
    def hamming_weight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count

    def test_one_bits(self):
        b = 0b00000000000000000000000000001011
        self.assertEqual(self.hamming_weight(b), 3)


"""
The expression n & (n-1) is a bitwise AND operation between n and n-1.

The effect of this operation is to clear the least significant bit that is set to 1 in n.

For example, let's say n is 10110 in binary (or 22 in decimal).

If we subtract 1 from n, we get 10101 in binary (or 21 in decimal), which has the same bits as n except for the least significant 1 bit.

If we now perform a bitwise AND between n and n-1, we get:
n   = 10110
n-1 = 10101
n & (n-1) = 10100
As you can see, the least significant 1 bit in n has been cleared, leaving only the higher-order 1 bits.

This operation clears exactly one 1 bit in each iteration of the loop, and the loop continues until all 1 bits have been cleared.
"""
