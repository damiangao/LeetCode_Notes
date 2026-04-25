class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        parent_val = preorder[0]
        for i,x in enumerate(inorder):
            if x == parent_val:
                mid = i
                break
        parent = TreeNode(parent_val)
        preorder_left = preorder[1:mid+1]
        preorder_right = preorder[mid+1:]
        inorder_left = inorder[:mid]
        inorder_right = inorder[mid+1:]

        parent.left = self.buildTree(preorder_left,inorder_left)
        parent.right = self.buildTree(preorder_right,inorder_right)
    
        return parent
