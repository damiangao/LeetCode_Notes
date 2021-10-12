class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        sorted_by_height = sorted(zip(height, weight), key=lambda x : (x[0], -x[1]))
        dp = [sorted_by_height[0][1]]
        for _, x in sorted_by_height:
            if x > dp[-1]:
                dp.append(x)
            else:
                pos = bisect.bisect_left(dp, x)
                dp[pos] = x
        return len(dp)
