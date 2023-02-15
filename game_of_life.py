import unittest


class GameOfLife(unittest.TestCase):
    """
    According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton
    devised by the British mathematician John Horton Conway in 1970."

    The board is made up of an m x n grid of cells, where each cell has an initial state:
    live (represented by a 1) or dead (represented by a 0).
    Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

    1) Any live cell with fewer than two live neighbors dies as if caused by under-population.
    2) Any live cell with two or three live neighbors lives on to the next generation.
    3) Any live cell with more than three live neighbors dies, as if by over-population.
    4) Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    The next state is created by applying the above rules simultaneously to every cell in the current state,
    where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
    """
    def game_of_life(self, board):
        """
        Do not return anything, modify board in-place instead.
        0 dead
        1 live
        2 dead -> live
        3 live -> dead
        """
        rows = len(board)
        cols = len(board[0])
        if rows == 0 or cols == 0:
            return
        # modify board in place using values 2 & 3 to update transitory states
        # use %2 to determine if the transitory states are considered live or dead (0, 2 = dead & 1, 3 = live)
        for row in range(rows):
            for col in range(cols):
                live_neighbors = sum([board[i][j]%2 for i in range(row-1,row+2) for j in range(col-1,col+2)
                                   if 0 <= i < rows and 0<= j < cols]) - board[row][col]
                # rule 4
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
                # rules 1, 2 & 3 (rule 2 is followed by not changing the value in cells with 2 or 2 live_neighbors)
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors >  3):
                    board[row][col] = 3
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == 3:
                    board[row][col] = 0
        return board

    def test_gol(self):
        input = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        output = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        self.assertEqual(self.game_of_life(input), output)