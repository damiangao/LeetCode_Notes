class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_ = sum(chalk)
        i = 0
        k %= sum_
        while chalk[i] <= k:
            k -= chalk[i]
            i += 1
        return i
