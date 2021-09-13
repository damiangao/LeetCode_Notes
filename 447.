class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ret = 0
        for x, y in points:
            dist_cnt = collections.defaultdict(int)
            for i, j in points:
                if i != x or j != y:
                    dist = (i - x) ** 2 + (j - y) ** 2
                    dist_cnt[dist] += 1
            for k, v in dist_cnt.items():
                ret += v * (v - 1)
        return ret
