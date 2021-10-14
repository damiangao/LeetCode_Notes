INT_MAX = 2 ** 31 - 1
INT_MIN = - 2 ** 31


class Solution:
    def myAtoi(self, s: str) -> int:
        states = {
            "start": {'digit': "in_number", 'blank': "start", 'symbol': "signed", 'x': "end"},
            "signed": {'digit': "in_number", 'blank': "end", 'symbol': "end", 'x': "end"},
            "in_number": {'digit': "in_number", 'blank': "end", 'symbol': "end", 'x': "end"},
            "end": {'digit': "end", 'blank': "end", 'symbol': "end", 'x': "end"}
        }

        symbol, ans, cur = 1, 0, "start"
        for i in s:
            if i == ' ':
                t = 'blank'
            elif i in ['+', '-']:
                t = 'symbol'
            elif i.isdigit():
                t = 'digit'
            else:
                t = 'x'
            cur = states[cur][t]
            if cur == "in_number":
                ans = ans * 10 + int(i)
                ans = min(INT_MAX, ans) if symbol == 1 else min(-INT_MIN, ans)
            elif cur == "signed":
                symbol = 1 if i == '+' else -1
        return symbol * ans
