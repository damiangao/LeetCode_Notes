class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        vis = {0}
        s = nums[0]
        
        for i in range(1, len(nums)):
            if (s + nums[i]) % k in vis:
                return True
            vis.add(s%k)
            s += nums[i]
        return False
