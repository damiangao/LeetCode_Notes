class Solution:
    def longestValidParentheses(self, s: str) -> int:
        c_s = [-1]
        ret = 0
        for i, x in enumerate(s):
            if x == '(':
                c_s.append(i)
            else:
                if len(c_s) > 1:
                    c_s.pop()
                    ret = max(ret, i - c_s[-1])
                else:
                    c_s[0] = i
        return ret
