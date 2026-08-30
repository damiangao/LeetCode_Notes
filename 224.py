class Solution:
    def calculate(self, s: str) -> int:
        opt = [1]
        sign = 1
        n = len(s)
        i=0
        ret =0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = opt[-1]
                i += 1
            elif s[i] == '-':
                sign = -opt[-1]
                i += 1
            elif s[i] == '(':
                opt.append(sign)
                i += 1
            elif s[i] == ')':
                opt.pop()
                i += 1
            else:
                num = 0 
                while i < n and s[i].isdigit():
                    num = num*10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
        return ret