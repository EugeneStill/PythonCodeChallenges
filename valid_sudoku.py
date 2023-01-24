import unittest
import collections

class ValidSudoku(unittest.TestCase):
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    """

    def valid_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # using defaultdict will set default value of key if key does not exist.
        # here, we use empty list to make it easier to append regardless of whether key already exists
        EMPTY_CHAR = "."
        boardMap = collections.defaultdict(list)
        print("\n")
        print(str(boardMap))
        for row in range(9):
            for col in range(9):
                char = board[row][col]
                if char != EMPTY_CHAR:
                    if char in boardMap:
                        for pos in boardMap[char]:
                            # use floor division to find values in same 3 x 3 sub-boxes
                            if (pos[0] == row) or (pos[1] == col) or (pos[0] // 3 == row // 3 and pos[1] // 3 == col // 3):
                                return False
                    boardMap[char].append((row, col))

        return True


    def test_valid_sudoku(self):
        board1 = [
              ["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        board2 = [
             ["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
        ]
        board3 = [
              ["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", "8", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]

        self.assertTrue(self.valid_sudoku(board1))
        self.assertFalse(self.valid_sudoku(board2))
        self.assertFalse(self.valid_sudoku(board3))



