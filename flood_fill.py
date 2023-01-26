import unittest

class FloodFill(unittest.TestCase):
    """
    An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

    You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
    of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color),
    and so on. Replace the color of all of the aforementioned pixels with color.

    Return the modified image after performing the flood fill.

    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
    all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: The starting pixel is already colored 0, so no changes are made to the image.
    """

    def flood_fill(self, image, sr, sc, new_color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows, cols = len(image), len(image[0])
        og_color = image[sr][sc]

        def isNotValidPixel(row, col):
            return (
                    row < 0 or row >= rows or
                    col < 0 or col >= cols)

        def isNotValidColor(row, col):
            return (
                    image[row][col] == new_color or
                    image[row][col] != og_color)

        def dfs(row, col):
            if isNotValidPixel(row, col): return
            if isNotValidColor(row, col): return

            image[row][col] = new_color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image

    def test_flood_fill(self):
        image1 = [[1,1,1],[1,1,0],[1,0,1]]
        expected1 = [[2,2,2],[2,2,0],[2,0,1]]
        image2 = [[0,0,0],[0,0,0]]
        expected2 = [[0,0,0],[0,0,0]]
        self.assertEqual(self.flood_fill(image1, 1, 1, 2), expected1)
        self.assertEqual(self.flood_fill(image2, 0, 0, 0), expected2)






