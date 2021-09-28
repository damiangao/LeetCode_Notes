# elegant solution
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.targetSum = targetSum
        self.trace = collections.defaultdict(int)
        self.trace[0] = 1
        return self.dfs(root, 0)
    def dfs(self, root, cur_sum):
        if not root:
            return 0
        cur_sum += root.val

        ret = self.trace[cur_sum - self.targetSum]
        self.trace[cur_sum] += 1
        ret += self.dfs(root.left, cur_sum)
        ret += self.dfs(root.right, cur_sum)
        self.trace[cur_sum] -= 1
        return ret
