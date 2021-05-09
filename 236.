# Lowest Common Ancestor (LCA)
# This code changed the way I think
# elegant solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.dfs(root, p, q)
        return self.ans

    def dfs(self, root, p, q):
        if not root:
            return False

        fleft = self.dfs(root.left, p, q)
        fright = self.dfs(root.right, p, q)
        if (fleft and fright) or ((root==p or root==q) and (fleft or fright)):
            self.ans = root
            return True
        return (root==p or root==q) or fleft or fright
