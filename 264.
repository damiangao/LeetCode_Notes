# elegant solution
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        p1, p2, p3 = 0, 0, 0
        for i in range(1, n):
            candidates = [dp[p1]*2, dp[p2]*3, dp[p3]*5]
            dp[i] = min(candidates)
            if dp[i] == candidates[0]:
                p1 += 1
            if dp[i] == candidates[1]:
                p2 += 1
            if dp[i] == candidates[2]:
                p3 += 1
        return dp[-1]
