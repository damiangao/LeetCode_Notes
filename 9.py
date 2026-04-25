class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversedNum = 0
        while reversedNum < x:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10
        return x == reversedNum or x == reversedNum // 10
