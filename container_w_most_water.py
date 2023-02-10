import unittest


class MaxArea(unittest.TestCase):
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
    of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The lines that will build the walls of the container holding the most water are at index 1 & index 8
    We compare the height of these 2 elements & use the shorter height * distance between the indeces to compute volume
    """

    def max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right, left = 0, len(height) - 1
        water = 0
        while right < left:
            water = max(water, (left - right) * min(height[right], height[left]))
            if height[right] < height[left]:
                right += 1
            else:
                left -= 1
        return water

    def test_max_area(self):
        input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        self.assertEqual(self.max_area(input), output)

