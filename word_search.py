import unittest


class SolWordSearch(unittest.TestCase):
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
    vertically neighboring. The same letter cell may not be used more than once.

    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true
    """
    def exist(self, board, word):
        if not board or len(word) > len(board) * len(board[0]):
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word):
                    print("RESTORED BOARD")
                    self.print_board(board)
                    return True
        print("RESTORED BOARD")
        self.print_board(board)
        return False

    # check whether we can find word, start at (row,col) position
    def dfs(self, board, row, col, word):
        # print("\n")
        # print("MAKING CALL FOR WORD {}".format(word))
        # self.print_board(board)
        if len(word) == 0: # all the characters are checked
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or word[0] != board[row][col]:
            return False

        # first character is found, check the remaining part
        tmp = board[row][col]
        # mark cell visited
        board[row][col] = "#"
        # check whether we can find decreasing length of remaining word
        # even though calls to dfs in 4 directions can be made we only make the calls until 1 call returns true
        # skip the remaining calls for the other directions in this iteration of checking res
        target = word[1:]
        res = self.dfs(board, row + 1, col, target) or self.dfs(board, row - 1, col, target) \
              or self.dfs(board, row, col + 1, target) or self.dfs(board, row, col - 1, target)
        # unmark cell to restore board
        print("UNMARKING CELL")
        board[row][col] = tmp
        return res

    def print_board(self,board):
        for row in board:
            row_chars = "".join([c for c in row])
            print(row_chars)
    def test_search(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        self.assertTrue(self.exist(board, word))

# LOGGING
# MAKING CALL FOR WORD ABCCED
# ABCE
# SFCS
# ADEE
# CHECKING A
#
#
# MAKING CALL FOR WORD BCCED
# #BCE
# SFCS
# ADEE
# CHECKING S
# RETURNING FALSE
#
#
# MAKING CALL FOR WORD BCCED
# #BCE
# SFCS
# ADEE
# CHECKING A
# RETURNING FALSE
#
#
# MAKING CALL FOR WORD BCCED
# #BCE
# SFCS
# ADEE
# CHECKING B
#
#
# MAKING CALL FOR WORD CCED
# ##CE
# SFCS
# ADEE
# CHECKING F
# RETURNING FALSE
#
#
# MAKING CALL FOR WORD CCED
# ##CE
# SFCS
# ADEE
# CHECKING D
# RETURNING FALSE
#
#
# MAKING CALL FOR WORD CCED
# ##CE
# SFCS
# ADEE
# CHECKING C
#
#
# MAKING CALL FOR WORD CED
# ###E
# SFCS
# ADEE
# CHECKING C
#
#
# MAKING CALL FOR WORD ED
# ###E
# SF#S
# ADEE
# CHECKING E
#
#
# MAKING CALL FOR WORD D
# ###E
# SF#S
# AD#E
# CHECKING NA
# RETURNING FALSE
#
#
# MAKING CALL FOR WORD D
# ###E
# SF#S
# AD#E
# CHECKING #
# RETURNING FALSE
#
#
# MAKING CALL FOR WORD D
# ###E
# SF#S
# AD#E
# CHECKING E
# RETURNING FALSE
#
#
# MAKING CALL FOR WORD D
# ###E
# SF#S
# AD#E
# CHECKING D
#
#
# MAKING CALL FOR WORD
# ###E
# SF#S
# A##E
# UNMARKING CELL
# UNMARKING CELL
# UNMARKING CELL
# UNMARKING CELL
# UNMARKING CELL
# UNMARKING CELL