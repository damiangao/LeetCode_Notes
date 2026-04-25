# not elegant solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        op = ['(', '[', '{']
        ed = [')', ']', '}']
        s = list(s)
        stack = []
        for x in s:
            if x in ed:
                if not stack:
                    return False
                else:
                    if x != ed[op.index(stack[-1])]:
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(x)
        
        if stack:
            return False
        return True

# elegant solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        brackets = {')':'(', ']':'[', '}':'{'}
        s = list(s)
        stack = []
        for x in s:
            if x in brackets:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if top != brackets[x]:
                        return False 
            else:
                stack.append(x)
        
        return not stack
