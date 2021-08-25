class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda inter: inter[1])
        end = intervals[0][1]
        ret = 1
        for x, y in intervals[1:]:
            if x >= end:
                ret += 1
                end = y
        return len(intervals) - ret
