class Solution(object):
    def __init__(self):
        self.ret = ""
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        curr = ""

        if not t:
            return curr
        
        curr = curr + str(t.val)
        if not t.left and not t.right:
            return curr
        curr = curr + '(' + self.tree2str(t.left) + ')'
        if t.right:
            curr = curr + '('  + self.tree2str(t.right) + ')'
        return curr
