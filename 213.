class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robline(nums[:-1]), self.robline(nums[1:]))

    def robline(self, nums: List[int]) -> int:
        n = len(nums)
        t1 = t2 = 0
        for i in reversed(range(n)):
            t1, t2 = max(t1, nums[i] + t2), t1
        return t1
