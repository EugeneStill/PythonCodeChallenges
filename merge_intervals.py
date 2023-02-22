import unittest


class MergeIntervals(unittest.TestCase):
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals.
    Return an array of the non-overlapping intervals that cover all the intervals in the input.
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    """
    def merge_intervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)
        return result

    def test_mi(self):
        input = [[1,3],[2,6],[8,10],[15,18]]
        output = [[1,6],[8,10],[15,18]]
        self.assertEqual(self.merge_intervals(input), output)
        input = [[1,3],[0,6]]
        output = [[0,6]]
        self.assertEqual(self.merge_intervals(input), output)