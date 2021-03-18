class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.dfs(root) != -1
    
    def dfs(self, root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l==-1 or r==-1:
            return -1
        diff = l - r
        if diff >= -1 and diff <= 1:
            return max(l,r) + 1
        return -1
