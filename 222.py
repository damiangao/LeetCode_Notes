class Solution:
    def countNodes(self, root: TreeNode) -> int:
        lh, rh = 0, 0
        l, r = root, root
        while l:
            l = l.left
            lh += 1
        while r:
            r = r.right
            rh += 1
        
        if lh == rh:
            return 2 ** lh - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
