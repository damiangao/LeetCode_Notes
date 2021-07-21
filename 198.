# states compression
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        t1 = t2 = 0
        for i in reversed(range(n)):
            t1, t2 = max(t1, nums[i] + t2), t1
        return t1
        
# buttom-top
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in reversed(range(n)):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        return dp[0]
  
# use memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = dict()
        def dp(i):
            if i < n:
                if i in memo:
                    return memo[i]
                memo[i] = max(dp(i+2) + nums[i], dp(i+1))
                return memo[i]
            else:
                return 0
        return dp(0)
        
# timeover
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(i):
            if i < n:
                return max(dp(i+2) + nums[i], dp(i+1))
            else:
                return 0
        return dp(0)
