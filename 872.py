# bad solution
class Solution(object):
    def __init__(self):
        self.l_leafs = []
        self.r_leafs = []
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.dfs(root1, self.l_leafs)
        self.dfs(root2, self.r_leafs)
        return operator.eq(self.l_leafs, self.r_leafs)
    
    def dfs(self, root, leafs):
        if root:
            self.dfs(root.left, leafs)
            if not root.left and not root.right:
                leafs.append(root.val)
            self.dfs(root.right, leafs)
