class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if not count:
                curr = num
                count = 1
            elif curr == num:
                count += 1
            else:
                count -=1
        return curr
