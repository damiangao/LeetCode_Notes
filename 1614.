class Solution:
    def maxDepth(self, s: str) -> int:
        ret = size = 0
        for char in s:
            if char == "(":
                size += 1
                ret = max(ret, size)
            elif char == ")":
                size -= 1
        return ret
