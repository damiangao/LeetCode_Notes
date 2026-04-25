class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        while i**2 <= c:
            if math.sqrt(c - i ** 2).is_integer():
                return True
            i += 1
        
        return False
