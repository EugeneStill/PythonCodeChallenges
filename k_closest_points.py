import heapq
import unittest


class KClosest(unittest.TestCase):
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
    return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

    Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    Output: [[3,3],[-2,4]]
    Explanation: The answer [[-2,4],[3,3]] would also be accepted.
    """
    def k_closest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # alt solution using sorting
        # return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:k]

        # Use min heap of size K.
        # For each item, we insert an item to our heap.
        # If inserting an item makes heap size larger than k,
        # Then we immediately pop LOWEST item after inserting new item using heappushpop
        # BC we are using the negative of the distance, the lowest value will be the highest Kth distance

        heap = []

        for (x, y) in points:
            dist = -(x * x + y * y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [[x, y] for (dist, x, y) in heap]

    def test_k(self):
        points = [[3,3],[5,-1],[-2,4]]
        expected_results = [[[3,3],[-2,4]], [[-2,4],[3,3]]]
        self.assertIn(self.k_closest(points, 2), expected_results)