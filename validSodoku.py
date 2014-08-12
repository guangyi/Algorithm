class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
      def isValidSudoku(self, board):
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] != '.':
                    if not self.isValid(row, col, board): return False
        return True
    def isValid(self, row, col, board):
        for c in range(0, 9):
            if board[row][c] == board[row][col] and c != col: return False
        for r in range(0, 9):
            if board[r][col] == board[row][col] and r != row: return False
        for r in range(row / 3 * 3, row / 3 * 3 + 3):
            for c in range(col / 3 * 3, col / 3 * 3 + 3):
                if board[r][c] == board[row][col] and r != row and c != col: return False
        return True