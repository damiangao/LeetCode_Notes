class Solution:
    def findComplement(self, num: int) -> int:
        highbit = 0
        for i in range(1, 31):
            if num >= (1 << i):
                highbit = i
            else:
                break
        mask = (1 << (highbit + 1)) - 1
        return num ^ mask
