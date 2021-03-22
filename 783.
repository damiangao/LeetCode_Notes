class Solution(object):
    def __init__(self):
        self.pre = None
        self.min_diff = float('inf')
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.min_diff
    
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            if self.pre != None:
                self.min_diff = min(self.min_diff, abs(root.val - self.pre))
            self.pre = root.val
            self.dfs(root.right)
