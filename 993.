class Solution(object):
    def __init__(self):
        self.depth = {}
        self.par ={}

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.dfs(root, None)
        return self.depth[x] == self.depth[y] and self.par[x] != self.par[y]
    
    def dfs(self, node, par):
        if node:
            self.depth[node.val] = self.depth[par.val] + 1 if par else 0
            self.par[node.val] = par

            self.dfs(node.left, node)
            self.dfs(node.right, node)
