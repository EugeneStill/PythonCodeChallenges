import unittest
import heapq
class Skyline(unittest.TestCase):

# https://leetcode.com/problems/the-skyline-problem/submissions/

    def get_skyline(self, buildings):
        MAX_HEAP_HEIGHT, MAX_HEAP_X, RESULT_X, RESULT_HEIGHT = 0, 1, 0, 1
        # get tuples of building coords + 0 height endpoints for right side of buildings
        x_height_right = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, "na") for L, R, H in buildings])
        result, max_heap = [[0, 0]], [(0, float("inf"))]

        for x, negative_height, right in x_height_right:
            # remove points from heap that are LEFT of x or same as x
            while x >= max_heap[0][MAX_HEAP_X]:
                heapq.heappop(max_heap)
            # add any points with height to heap
            if negative_height:
                heapq.heappush(max_heap, (negative_height, right))
            # get cmh, if cmh != height of most recent result height then add x, cmh to result
            curr_max_height = -max_heap[0][MAX_HEAP_HEIGHT]
            if curr_max_height != result[-1][RESULT_HEIGHT]:
                result.append([x, curr_max_height])
        return result[1:]


    def test_skyline(self):
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
        result = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        self.assertEqual(self.get_skyline(buildings), result)