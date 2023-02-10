import unittest


class TrappingRainWater(unittest.TestCase):
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water (how many units, not volume) it can trap after raining.
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
    In this case, 6 units of rain water (blue section) are being trapped.
    """
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0

        ans, left, right = 0, 1, len(height) - 1
        lmax, rmax = height[0], height[-1]
        # print("\n")
        while left <= right:
            # check lmax and rmax for current right, left positions
            if height[left] > lmax:
                lmax = height[left]
            if height[right] > rmax:
                rmax = height[right]
            # print("LEFT {} LMAX {} RMAX {} RIGHT {}".format(left, lmax, rmax, right))

            # fill water upto lmax level for index left and move left to the right
            if lmax <= rmax:
                ans += lmax - height[left]
                left += 1
                # print("MOVING LEFT.  ANS {}".format(ans))

            # fill water upto rmax level for index right and move right to the left
            else:
                ans += rmax - height[right]
                right -= 1
                # print("MOVING RIGHT.  ANS {}".format(ans))

        return ans

    def test_water(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        output = 6
        self.assertEqual(self.trap(height), output)


# LOGGING
# LEFT 1 LMAX 1 RMAX 1 RIGHT 11
# MOVING LEFT.  ANS 0
# LEFT 2 LMAX 1 RMAX 1 RIGHT 11
# MOVING LEFT.  ANS 1
# LEFT 3 LMAX 2 RMAX 1 RIGHT 11
# MOVING RIGHT.  ANS 1
# LEFT 3 LMAX 2 RMAX 2 RIGHT 10
# MOVING LEFT.  ANS 1
# LEFT 4 LMAX 2 RMAX 2 RIGHT 10
# MOVING LEFT.  ANS 2
# LEFT 5 LMAX 2 RMAX 2 RIGHT 10
# MOVING LEFT.  ANS 4
# LEFT 6 LMAX 2 RMAX 2 RIGHT 10
# MOVING LEFT.  ANS 5
# LEFT 7 LMAX 3 RMAX 2 RIGHT 10
# MOVING RIGHT.  ANS 5
# LEFT 7 LMAX 3 RMAX 2 RIGHT 9
# MOVING RIGHT.  ANS 6
# LEFT 7 LMAX 3 RMAX 2 RIGHT 8
# MOVING RIGHT.  ANS 6
# LEFT 7 LMAX 3 RMAX 3 RIGHT 7
# MOVING LEFT.  ANS 6