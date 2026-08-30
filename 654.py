class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# basic: 递归找最大值,左右分治。O(n^2) 最坏(有序数组时每层都要线性找max)
class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        i = nums.index(max(nums))
        node = TreeNode(nums[i])
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i+1:])
        return node


# elegant: 单调栈 O(n)。栈 = 当前树的右脊柱(从根一路向右走的链),栈底到栈顶严格递减
# 每个元素入栈一次出栈一次 -> O(n)
class SolutionStack:
    def constructMaximumBinaryTree(self, nums):
        stack = []
        for v in nums:
            node = TreeNode(v)
            last = None
            while stack and stack[-1].val < v:
                last = stack.pop()      # 比 v 小的弹栈:整条链归入 v 的左子树
            node.left = last            # 最后弹出的就是这条链的链头
            if stack:
                stack[-1].right = node  # 栈顶比 v 大:v 是它的右孩子
            stack.append(node)
        return stack[0] if stack else None  # 栈底永远是当前根


if __name__ == '__main__':
    def to_list(root):
        # 层序展开(带 null,末尾去 null),模仿 LeetCode 输出
        out, q = [], [root]
        while q:
            n = q.pop(0)
            if n is None:
                out.append(None)
                continue
            out.append(n.val)
            q.append(n.left)
            q.append(n.right)
        while out and out[-1] is None:
            out.pop()
        return out

    a, b = Solution(), SolutionStack()
    for nums in ([3, 2, 1, 6, 0, 5], [2, 3, 1], [1], []):
        assert to_list(a.constructMaximumBinaryTree(list(nums))) == \
               to_list(b.constructMaximumBinaryTree(list(nums)))
    # LeetCode 官方例子的期望输出
    assert to_list(b.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])) == \
           [6, 3, 5, None, 2, 0, None, None, 1]
    print('ok')
