class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l+r) >> 1
            if mid**2 > x:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans//1
