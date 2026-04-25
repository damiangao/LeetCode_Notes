class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        while s[n] == ' ':
            n -= 1
        a = n
        while n >= 0 and s[n] != ' ':
            n -= 1
        return a - n
