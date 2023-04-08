class KthSmallest(object):
    """
    The algorithm uses binary search to find the kth smallest element in the matrix.
    It initializes the search range to be between the smallest and largest elements in the matrix.
    Then, it defines a helper function check(m) which counts the number of elements in the matrix that are less than
    or equal to the input value m. The check(m) function uses a two-pointer approach to traverse the matrix in O(n) time
    counting the number of elements that are less than or equal to m.

    The binary search loop iterates until the beg and end pointers converge,
    at which point beg points to the kth smallest element.
    The binary search loop performs O(log (max-min)) iterations since it halves the search range at each iteration.

    Therefore, the overall time complexity is O(n log (max-min)).

    The space complexity of the code is O(1)
    """
    def kth_smallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, beg, end = len(matrix), matrix[0][0], matrix[-1][-1]

        def check(m):
            row, col, cnt = 0, rows - 1, 0
            for row in range(rows):
                while col >= 0 and matrix[row][col] > m:
                    col -= 1
                cnt += (col + 1)
            return cnt

        while beg < end:
            mid = (beg + end) // 2
            if check(mid) < k:
                beg = mid + 1
            else:
                end = mid

        return beg



