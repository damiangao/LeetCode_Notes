class Solution(object):
    def isValidBST(self, root):
        return self.dfs(root, None, None)

    def dfs(self, root, min_, max_):
        if not root:
            return True
        if min_ and root.val <= min_.val:
            return False
        if max_ and root.val >= max_.val:
            return False
        return self.dfs(root.left, min_, root) and self.dfs(root.right, root, max_)
