class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return res
        q = deque([root])
        level = 1
        while q:
            curr_level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                curr_level.append(curr.val)
            if level % 2 == 0:
                curr_level.reverse()
            res.append(curr_level)
            level = level + 1
        return res
