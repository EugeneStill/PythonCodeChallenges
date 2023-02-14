import heapq as hq
import unittest


class MedianFinder():
    """
    The median is the middle value in an ordered integer list. If the size of the list is even,
    there is no middle value, and the median is the mean of the two middle values.

    For arr = [2,3,4], the median is 3.
    For arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    addNum(int num) adds the integer num from the data stream to the data structure.
    findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


    *** heapq only has minheap. so we use '-' values to make our min a max heap
    """


    def __init__(self):
        self.lo = []
        self.hi = []

    def add_num(self, num):
        # add num to appropriate heap
        if not self.lo:
            hq.heappush(self.lo, -num)
        elif num <= -self.lo[0]:
            hq.heappush(self.lo, -num)
        else:
            hq.heappush(self.hi, num)
        # rebalance so that lo is always equal to or 1 longer than hi
        if len(self.lo) > len(self.hi) + 1:
            hq.heappush(self.hi, -hq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            hq.heappush(self.lo, -hq.heappop(self.hi))

    def find_median(self):
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0]) / 2.0
        return -self.lo[0]

class test_median(unittest.TestCase):

    def test_median(self):
        mf = MedianFinder();
        mf.add_num(1)  # arr = [1]
        mf.add_num(2)  # arr = [1, 2]
        self.assertEqual(mf.find_median(), 1.5)
        mf.add_num(3) # arr[1, 2, 3]
        self.assertEqual(mf.find_median(), 2.0)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()