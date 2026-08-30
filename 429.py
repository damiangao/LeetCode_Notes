"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ret = []

        q = deque([root])
        while q:
            layer = []
            for i in range(len(q)):
                curr = q.popleft()
                layer.append(curr.val)
                if curr.children:
                    for child in curr.children:
                        q.append(child)
                
            ret.append(layer)
        return ret
                