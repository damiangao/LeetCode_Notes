# elegant solution 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return max(m, n)
        
        dp = [[0] * (n+1) for _ in range(m + 1)]
        
        for i in range(n + 1):
            dp[0][i] = i
        
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = dp[i][j-1] + 1
                down = dp[i-1][j] + 1
                left_down = dp[i-1][j-1] + 1

                if word1[i-1] == word2[j-1]:
                    left_down -= 1
                
                dp[i][j] = min(left, down, left_down)
        return dp[m][n]
