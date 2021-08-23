class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_ = max(piles)
        l, r = 1, max_ + 1
        while l < r:
            mid = l + ((r - l) >> 2)
            if self.can(piles, mid, h):
                r = mid
            else:
                l = mid + 1
        return l
        
    def can(self, piles, k, h):
        cost = 0
        for x in piles:
            cost += math.ceil(x / k)
        return cost <= h
