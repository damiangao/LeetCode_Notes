# memo
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            
            res = float('inf')
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1:
                    continue
                res = min(res, sub + 1)
            memo[n] = res if res != float('inf') else -1
            return memo[n]

        return dp(amount)

# array iteration
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
