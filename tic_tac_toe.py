class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # Update the board with the player's move
        self.board[row][col] = player

        # Check for a win in the row
        if all(self.board[row][j] == player for j in range(self.n)):
            return player

        # Check for a win in the column
        if all(self.board[i][col] == player for i in range(self.n)):
            return player

        # Check for a win in the diagonal (top-left to bottom-right)
        if row == col and all(self.board[i][j] == player for i, j in zip(range(self.n), range(self.n))):
            return player

        # Check for a win in the diagonal (bottom-left to top-right)
        if row + col == self.n - 1 and all(
                self.board[i][j] == player for i, j in zip(range(self.n), range(self.n - 1, -1, -1))):
            return player

        # No winner yet
        return 0
