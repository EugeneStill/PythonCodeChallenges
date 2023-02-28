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
        for right, current_height in enumerate(heights):
            # whenever previous height > current_height check for bigger rectangle
            while s and heights[s[-1]] > current_height:
                prev_height = heights[s.pop()]
                left = s[-1]
                # subtract 1 extra because we have already moved right past the prev_height that we are checking
                area = (right-left-1) * prev_height
                res = max(res, area)
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

# LOGGING
# [0, 2, 1, 5, 6, 2, 3, 0]
# RIGHT 0 HEIGHT 0 S [0]
# RIGHT 1 HEIGHT 2 S [0, 1]
#
# LEFT 0 RIGHT 2 CURRENT HEIGHT 1 LAST HEIGHT 2
# RES IS 2
#
# RIGHT 2 HEIGHT 1 S [0, 2]
# RIGHT 3 HEIGHT 5 S [0, 2, 3]
# RIGHT 4 HEIGHT 6 S [0, 2, 3, 4]
#
# LEFT 3 RIGHT 5 CURRENT HEIGHT 2 LAST HEIGHT 6
# RES IS 6
#
#
# LEFT 2 RIGHT 5 CURRENT HEIGHT 2 LAST HEIGHT 5
# RES IS 10
#
# RIGHT 5 HEIGHT 2 S [0, 2, 5]
# RIGHT 6 HEIGHT 3 S [0, 2, 5, 6]
#
# LEFT 5 RIGHT 7 CURRENT HEIGHT 0 LAST HEIGHT 3
# RES IS 10
#
#
# LEFT 2 RIGHT 7 CURRENT HEIGHT 0 LAST HEIGHT 2
# RES IS 10
#
#
# LEFT 0 RIGHT 7 CURRENT HEIGHT 0 LAST HEIGHT 1
# RES IS 10
#
# RIGHT 7 HEIGHT 0 S [0, 7]
# PASSED

