import unittest
class ZigZag(unittest.TestCase):
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    """
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        answer = [""] * numRows
        row_idx = 1
        going_down = True

        for c in s:
            answer[row_idx-1] += c
            if row_idx == numRows:
                going_down = False
            if row_idx == 1:
                going_down = True

            if going_down:
                row_idx += 1
            else:
                row_idx -= 1
        return "".join(answer)

    def test_convert(self):
        input_str, numRows = "PAYPALISHIRING", 3
        expected_str = "PAHNAPLSIIGYIR"
        self.assertEqual(self.convert(input_str, 3), expected_str)