import unittest


class InsertInterval(unittest.TestCase):
    """
    You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
    the start and the end of the ith interval and intervals is sorted in ascending order by starti.
    You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
    still does not have any overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
    """
    def insert_interval(self, intervals, new_interval):
        """
        :type intervals: List[List[int]]
        :type new_interval: List[int]
        :rtype: List[List[int]]
        """
        # get 3 lists of intervals:
        # 1 all intervals that end before new interval start
        # 2 all intervals that start after new interval end
        # 3 the new interval that could include any existing intervals that end after ni start or start before ni end
        START, END = 0, 1
        left, right, insert = [], [], []
        insert_start, insert_end = new_interval[START], new_interval[END]

        for i in intervals:
            if i[END] < insert_start:
                left.append(i)
            elif i[START] > insert_end:
                right.append(i)
            else:
                insert_start = min(insert_start, i[START])
                insert_end = max(insert_end, i[END])
        insert.append([insert_start, insert_end])
        return left + insert + right


    def test_insert(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expected_result = [[1,2],[3,10],[12,16]]
        self.assertEqual(self.insert_interval(intervals, newInterval), expected_result)