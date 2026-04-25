class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        squares = [[[0] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch != '.':
                    ch = ord(ch) - ord('1')
                    rows[i][ch] += 1
                    cols[j][ch] += 1
                    squares[i//3][j//3][ch] += 1

                    if rows[i][ch] > 1 or cols[j][ch] > 1 or squares[i//3][j//3][ch] > 1:
                        return False
        return True
