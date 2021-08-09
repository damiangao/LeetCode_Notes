class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum, ret = 0, 0
        count = collections.defaultdict(int)
        count[0] = 1
        for x in nums:
            cur_sum += x
            ret += count[cur_sum - k]
            count[cur_sum] += 1
        return ret
