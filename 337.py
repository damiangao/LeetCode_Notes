class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = dict()

        def dp(node):
            if not node:
                return 0
            else:
                if node in memo:
                    return memo[node]

                do = node.val + (dp(node.left.left) + dp(node.left.right) if node.left else 0) + \
                     (dp(node.right.left) + dp(node.right.right) if node.right else 0)
                not_do = dp(node.left) + dp(node.right)
                memo[node] = max(do, not_do)
                return memo[node]

        return dp(root)
