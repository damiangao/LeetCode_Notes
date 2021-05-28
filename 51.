# not elegant solution
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        board = [['.'] * n for _ in range(n)]
        self.ret = []
        self.backtrack(board, 0)
        return self.ret
    
    def backtrack(self, board, row):
        if row == self.n:
            self.ret.append(list(map(lambda x: "".join(x), board)))
            return
        for col in range(self.n):
            board[row][col] = 'Q'
            if self.check(board, row, col):
                self.backtrack(board, row + 1)
            board[row][col] = '.'

    def check(self, board, row, col):
        for r in range(row):
            if board[r][col] == 'Q':
                return False
        
        for r, c in zip(reversed(range(row)), reversed(range(col))):
            if board[r][c] == 'Q':
                return False
        
        for r, c in zip(reversed(range(row)), range(col + 1, self.n)):
            if board[r][c] == 'Q':
                return False
        
        return True
