class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        q = deque([root])
        res = []
        while q:
            layer = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
                layer.append(curr.val)
            res.append(layer)
        
        return res[-1][0]
