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
        print("\n")
        while left <= right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])

            # fill water up to lmax level for index left and move left to the right
            if lmax <= rmax:
                ans += lmax - height[left]
                print("ANS {} LMAX {} LEFT {} RMAX {} RIGHT {} MOVING LEFT=>".format(ans, lmax, left, rmax, right))
                left += 1

            # fill water up to rmax level for index right and move right to the left
            else:
                ans += rmax - height[right]
                print("ANS {} LMAX {} LEFT {} RMAX {} RIGHT {} <= MOVING RIGHT.".format(ans, lmax, left, rmax, right))
                right -= 1

        return ans

    def test_water(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        output = 6
        self.assertEqual(self.trap(height), output)


# LOGGING
# ANS 0 LMAX 1 LEFT 1 RMAX 1 RIGHT 11 MOVING LEFT=>
# ANS 1 LMAX 1 LEFT 2 RMAX 1 RIGHT 11 MOVING LEFT=>
# ANS 1 LMAX 2 LEFT 3 RMAX 1 RIGHT 11 <= MOVING RIGHT.
# ANS 1 LMAX 2 LEFT 3 RMAX 2 RIGHT 10 MOVING LEFT=>
# ANS 2 LMAX 2 LEFT 4 RMAX 2 RIGHT 10 MOVING LEFT=>
# ANS 4 LMAX 2 LEFT 5 RMAX 2 RIGHT 10 MOVING LEFT=>
# ANS 5 LMAX 2 LEFT 6 RMAX 2 RIGHT 10 MOVING LEFT=>
# ANS 5 LMAX 3 LEFT 7 RMAX 2 RIGHT 10 <= MOVING RIGHT.
# ANS 6 LMAX 3 LEFT 7 RMAX 2 RIGHT 9 <= MOVING RIGHT.
# ANS 6 LMAX 3 LEFT 7 RMAX 2 RIGHT 8 <= MOVING RIGHT.
# ANS 6 LMAX 3 LEFT 7 RMAX 3 RIGHT 7 MOVING LEFT=>