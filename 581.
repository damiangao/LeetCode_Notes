class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = sorted(nums)
        l, r = 0, len(nums) - 1
        while l < len(nums) and nums[l] == temp[l]:
            l += 1
        while r >= 0 and nums[r] == temp[r]:
            r -= 1
        
        return r - l + 1 if l < r else 0
