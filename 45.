class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        farthest = 0
        ret = 0
        for i, x in enumerate(nums[:-1]):
            farthest = max(farthest, x + i)
            if i == end:
                end = farthest
                ret += 1
        return ret
