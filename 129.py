# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, pre):
        if not root:
            return 0

        total = 0
        pre = pre*10 + root.val
      
        if root.left:
            total += self.dfs(root.left, pre)
        if root.right:
            total += self.dfs(root.right, pre)

        if not root.left and not root.right:
            return pre

        return total



    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        

