class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        x = len(strs)
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(x+1)]

        for i in range(1, x+1):
            zeros = strs[i-1].count('0')
            ones = strs[i-1].count('1')

            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-zeros][k-ones] + 1)
        return dp[x][m][n]
