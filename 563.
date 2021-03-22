class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, tilt = self.dfs(root)
        return tilt
    def dfs(self, root):
        if not root:
            return 0, 0
        l_s, l_t = self.dfs(root.left)
        r_s, r_t = self.dfs(root.right)
        val_sum = l_s + r_s + root.val
        tilt_sum = l_t + r_t + abs(l_s - r_s)
        return val_sum, tilt_sum
