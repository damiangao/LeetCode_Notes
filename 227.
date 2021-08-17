class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            c = s[i]
            if c.isalnum():
                num = 10 * num + int(c)
            if not c.isalnum() and c != ' ' or i == len(s) - 1:
                
                if sign == '+':
                    stk.append(num)
                elif sign == '-':
                    stk.append(-num)
                elif sign == '*':
                    pre = stk.pop()
                    stk.append(pre * num)
                elif sign == '/':
                    pre = stk.pop()
                    if pre < 0:
                        stk.append(-(abs(pre) // num))
                    else:
                        stk.append(pre // num)
                sign = c
                num = 0
        ret = 0
        while stk:
            ret += stk.pop()
        return ret
