import unittest


class PascalsTriangle(unittest.TestCase):
    def get_row(self, row_index):
        """
        :type row_index: int
        :rtype: List[int]
        """
        row = [1] * (row_index + 1)
        if row_index == 0:
            return row
        print("MAKING RECURSION CALL FOR ROW {}".format(row_index))
        prev_row = self.get_row(row_index - 1)
        print("BUILDING OUT ROW {}".format(row_index))
        for i in range(1, len(row)-1):
            row[i] = prev_row[i-1] + prev_row[i]
        print("ROW {}: {}".format(row_index, str(row)))
        return row

    def test_kth_row(self):
        self.get_row(3)