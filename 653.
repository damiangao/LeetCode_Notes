class Solution(object):
    def __init__(self):
        self.all_num = {}
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.dfs(root)
        for key in self.all_num.keys():
            if (k - key) in self.all_num:
                if key != k - key:
                    return True
                if self.all_num[key] > 1:
                    return True
        return False
    def dfs(self, root):
        if root:
            if root.val in self.all_num:
                self.all_num[root.val] = self.all_num[root.val] + 1
            else:
                self.all_num[root.val] = 1
            self.dfs(root.left)
            self.dfs(root.right)
