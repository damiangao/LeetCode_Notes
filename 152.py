#elegant solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return []

        min_dp = []
        max_dp = []

        for x in nums:

            if not min_dp or not min_dp[-1] or not x:
                min_dp.append(x)
                max_dp.append(x)
                continue

            min_cur = min(x, x*min_dp[-1], x*max_dp[-1])
            max_cur = max(x, x*min_dp[-1], x*max_dp[-1])

            min_dp.append(min_cur)
            max_dp.append(max_cur)

        return max(max_dp)
