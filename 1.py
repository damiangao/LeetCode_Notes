class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i, num in enumerate(nums):
            hashMap[num] = i

        for i, num in enumerate(nums):
            other = target - num
            if other in hashMap and hashMap[other] != i:
                return [i, hashMap[other]]
                
# elegant solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i, x in enumerate(nums):
            other = target - x
            if (idx := hashset.get(other)) != None:
                return [idx, i]
            hashset[x] = i
