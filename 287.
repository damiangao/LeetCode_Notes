class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = nums[0], nums[nums[0]]
        while l != r:
            l = nums[l]
            r = nums[nums[r]]
        l = 0
        while l != r:
            l = nums[l]
            r = nums[r]
        return l
