class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2) 
        else:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
    
# smart way
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 3:
            return 2
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2) 
        else:
            if (n & 3) == 3:
                return 1 + self.integerReplacement(n+1)
            else:
                return 1 + self.integerReplacement(n-1)
    
