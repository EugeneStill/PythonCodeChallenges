import unittest


class LargestRectangleArea(unittest.TestCase):
    """
    Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
    return the area of the largest rectangle in the histogram.

    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.
    """
    def largest_rectangle_area(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        s = []
        heights = [0] + heights + [0]
        print("\n{}".format(str(heights)))
        for right, height in enumerate(heights):
            print("RIGHT {} HEIGHT {}".format(right, height))
            while s and heights[s[-1]] > height:
                print("CHECKING RIGHT {} CURRENT HEIGHT {} LAST HEIGHT {}".format(right, height, heights[s[-1]]))
                prev_rect = s.pop()
                left = s[-1]
                area = (right-left-1) * heights[prev_rect]
                res = max(res, area)
                print("RES IS {}".format(res))
            s.append(right)
        return res

        # heights.append(0)
        # stack = [-1]
        # ans = 0
        # print("\n")
        # for i in range(len(heights)):
        #     print("CHECKING I {} HEIGHT I {} HEIGHT STACK-1 {}".format(i, heights[i], heights[stack[-1]]))
        #     while heights[i] < heights[stack[-1]]:
        #         h = heights[stack.pop()]
        #         w = i - stack[-1] - 1
        #         print("H {} W {}".format(h, w))
        #         ans = max(ans, h * w)
        #     stack.append(i)
        ## restore heights to original values
        # heights.pop()
        # return ans

    def test_lra(self):
        self.assertEqual(self.largest_rectangle_area([2,1,5,6,2,3]), 10)