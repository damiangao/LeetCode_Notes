# elegant solution
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            hint = guess(mid)
            if hint == -1:
                r = mid - 1
            elif hint == 0:
                return mid
            elif hint == 1:
                l = mid + 1
