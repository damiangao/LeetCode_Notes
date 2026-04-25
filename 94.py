# elegant solution
class Solution(object):
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.res.append(root.val)    
        self.dfs(root.right)    
