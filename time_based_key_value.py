import collections
import unittest
import collections

class TimeMap(object):
    """
    Design a time-based key-value data structure that can store multiple values for the same key at different
    timestamps and retrieve the key's value at a certain timestamp.

    Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    set Stores the key  with the value at the given timestamp.
    get Returns a value such that set was called previously, with timestamp_prev <= timestamp.
    If there are multiple such values, return value with the largest timestamp_prev. If there are no values, return "".
    """

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        arr = self.dic.get(key, [])
        l, r = 0, len(arr)

        while l < r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                l = mid + 1
            elif arr[mid][0] > timestamp:
                r = mid
        # r is index of smallest element > timestamp. r -1 is the one we need to return
        return "" if r == 0 else arr[r - 1][1]

class TestMap(unittest.TestCase):
    def test_time_map(self):
        timeMap = TimeMap()
        timeMap.set("foo", "bar", 1)
        self.assertEqual(timeMap.get("foo", 1), "bar")
        self.assertEqual(timeMap.get("foo", 3), "bar")
        timeMap.set("foo", "bar2", 4)
        self.assertEqual(timeMap.get("foo", 4), "bar2")
        self.assertEqual(timeMap.get("foo", 4), "bar2")

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)