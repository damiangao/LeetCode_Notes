class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum_ = 1
        d = 2
        while d**2 <= num:
            if num%d == 0:
                sum_ += d
                if d**2 != num:
                    sum_ += num//d
            d += 1
        return sum_ == num
