class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root==nullptr)
            return 0;
        int left = minDepth(root->left);
        int right = minDepth(root->right);

        if(left == 0)
            return right + 1;
        else if(right == 0)
            return left + 1;

        return min(left, right) + 1;
    }
};

# python
# bad solution
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
            
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# elegant solution
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = collections.deque([root])
        ans = 1

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    return ans
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans += 1
