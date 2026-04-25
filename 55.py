class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i, x in enumerate(nums[:-1]):
            farthest = max(farthest, nums[i] + i)
            if farthest <= i:
                return False
        return farthest >= n - 1
