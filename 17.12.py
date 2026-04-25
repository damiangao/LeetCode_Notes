class Solution(object):
    def __init__(self):
        self.link = []
    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.dfs(root)
        pre = self.link[0]
        pre.left = None
        for i in range(1, len(self.link)):
            pre.right = self.link[i]
            pre = self.link[i]
            pre.left = None
        pre.right = None
        return self.link[0]
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            self.link.append(root)
            self.dfs(root.right)
