class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum = collections.defaultdict(int)
        presum[0] = 1
        res, curr_sum = 0, 0
        for x in nums:
            curr_sum += x
            res += presum[curr_sum - goal]
            presum[curr_sum] += 1
        return res
