class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = sum_ = 0
        n = len(nums)
        ret = n + 1
        while r < n:
            sum_ += nums[r]
            while sum_ >= target:
                ret = min(ret, r - l + 1)
                sum_ -= nums[l]
                l += 1
            r += 1
        return 0 if ret > n else ret
