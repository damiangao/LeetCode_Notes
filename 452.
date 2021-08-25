class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda inter: inter[1])
        end = points[0][1]
        ret = 1
        for x, y in points[1:]:
            if x > end:
                ret += 1
                end = y
        return ret
