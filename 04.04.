class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bl, _ = self.dfs(root)
        return bl
    def dfs(self, root):
        if not root:
            return True, 0
        
        l, ld = self.dfs(root.left)
        r, rd = self.dfs(root.right)

        bl = l and r and abs(ld - rd) < 2
        deep = max(ld, rd) + 1
        return bl, deep
