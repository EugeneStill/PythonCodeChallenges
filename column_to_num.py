import unittest


class ColumnToNumber(unittest.TestCase):
    """
    Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

    For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
    """
    def col_to_num(self, column_title):
        """
        :type columnTitle: str
        :rtype: int
        """
        col_num = 0
        for char in column_title:
            col_num = col_num * 26 + (ord(char) - 64)
        return col_num

    def test_col_to_num(self):
        self.assertEqual(self.col_to_num('A'), 1)
        self.assertEqual(self.col_to_num('AA'), 27)
