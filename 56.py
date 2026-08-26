class Solution:
    def merge_single(self,a,b):
        return [a[0], max(a[1],b[1])]
    def can_merge(self,a,b):
        return a[1]>=b[0]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        56. Merge Intervals
        Medium

        合并重叠的区间
        """
        ret = []
        intervals=sorted(intervals, key=lambda x:x[0])

        if len(intervals) <=1:
            return intervals
        curr = intervals[0]
        i = 1
        while i < len(intervals):
            if self.can_merge(curr, intervals[i]):
                curr =self.merge_single(curr, intervals[i])
            else:
                ret.append(curr)
                curr = intervals[i]
            i += 1

        ret.append(curr)
        return ret
