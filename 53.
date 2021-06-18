# elegant solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = t0 = nums[0]
        for x in nums[1:]:
            t0 = max(t0 + x, x)
            res = max(t0, res)
        return res

# not elegant solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)
