# easy & elegant solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            i = bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)

# elegant solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float('inf')]
        for i in range(n):
            length = len(dp)
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            l, r = 0, length-1
            while l <= r:
                mid = (l+r)>>1
                if nums[i] < dp[mid] and nums[i] > dp[mid-1]:
                    dp[mid] = nums[i]
                    break
                elif nums[i] < dp[mid]:
                    r = mid-1
                elif nums[i] >= dp[mid]:
                    l = mid+1

        return len(dp) - 1
        
# not best
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        n = len(nums)
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
