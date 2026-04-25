class Solution:
    def __init__(self):
        self.ret = []

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.trackback(root, [])
        return self.ret
    
    def trackback(self, root, trace):
        if root:
            trace.append(str(root.val))
            if not root.left and not root.right:
                self.ret.append('->'.join(trace))
            self.trackback(root.left, trace)
            self.trackback(root.right, trace)
            trace.pop()
