# my elegant solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = []
        for x in nums:
            if x > n:
                x = x - n
            x = abs(x) - 1
            if nums[x] > 0:
                nums[x] = -nums[x]
            else:
                nums[x] = -nums[x] + n
        for i, x in enumerate(nums):
            if x > n:
                ret.append(i+1)
        return ret
