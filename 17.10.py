class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr, count = None, 0
        for x in nums:
            if curr == None:
                curr, count = x, 1
                continue
            if x == curr:
                count += 1
            else:
                count -= 1
                if count == 0:
                    curr = None
        count = 0
        for x in nums:
            if x == curr:
                count += 1
        
        return curr if count*2 > len(nums) else -1
            

