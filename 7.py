class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 1 if x > 0 else -1
        x = str(abs(x))[::-1]
        x = int(x)
        if ret < 0:
            x = x if x <= 2**31 else 0
        if ret > 0:
            x = x if x < 2**31 else 0
        return ret * x
