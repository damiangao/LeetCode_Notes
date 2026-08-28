# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTreesRange(self, l,r):
        ret = []
        if l > r:
            return [None]

        for i in range(l, r+1):
            left_trees = self.generateTreesRange(l, i-1)
            right_trees = self.generateTreesRange(i + 1, r)
            for left in left_trees:
                for right in right_trees:
                    ret.append(TreeNode(i,left,right))
        return ret

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTreesRange(1,n)
        
        

