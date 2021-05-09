class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                strs = ""
                while stack[-1] != '[':
                    strs = stack.pop() + strs
                stack.pop() # deal [
                times = ""
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times
                tiems = int(times)
                stack.extend([strs] * tiems)
        return "".join(stack)
