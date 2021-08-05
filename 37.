class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)

    def isValid(self, board, r, c, n):
        for i in range(9):
            if board[i][c] == n:
                return False
            if board[r][i] == n:
                return False
            if board[r//3*3 + i//3][c//3*3 + i%3] == n:
                return False
        return True

    def backtrack(self, board, i, j):
        m, n = 9, 9
        if j == n:
            return self.backtrack(board, i + 1, 0)
        if i == m:
            return True
        if board[i][j] != '.':
            return self.backtrack(board, i, j + 1)
        for ch in range(ord('1'), ord('9') + 1):
            if not self.isValid(board, i, j, chr(ch)):
                continue

            board[i][j] = chr(ch)
            if self.backtrack(board, i, j + 1):
                return True
            board[i][j] = '.'

