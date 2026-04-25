class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        return '[' + ','.join(self.preorder_read(root)) + ']'
        

    
    def preorder_read(self, root):
        if not root:
            return ['null']
        return  [str(root.val)] + self.preorder_read(root.left) + self.preorder_read(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data[1:-1].split(',')
        queue = collections.deque(data)
        return self.preorder_build(queue)


    def preorder_build(self, queue):
        if not queue:
            return None
        
        first = queue.popleft()
        if first == 'null':
            return None
        
        root = TreeNode(int(first))
        root.left = self.preorder_build(queue)
        root.right = self.preorder_build(queue)
        return root  
