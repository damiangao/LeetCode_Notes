//Best
class Solution {
public:
    int ret = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        depth(root);
        return ret;
    }
    int depth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int l = depth(root->left);
        int r = depth(root->right);
        ret = max(ret, l + r);
        return max(l, r) + 1;
    }
};

//Mine
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int depth = 0;
        return dfs(root, depth);
    }

    int dfs(TreeNode* root, int &depth){
        if(root == nullptr){
            depth = 0;
            return 0;
        }
        int L_mx = dfs(root->left, depth);
        int ld = depth;
        int R_mx = dfs(root->right, depth);
        int rd = depth;
        depth = 1 + max(ld, rd);
        return max(max(L_mx, R_mx), ld + rd);
    }
};

# python 
# elegant solution
class Solution(object):
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.ans 
    def dfs(self, root):
        if not root:
            return 0
        
        l_depth = self.dfs(root.left)
        r_depth = self.dfs(root.right)
        self.ans = max(self.ans, l_depth + r_depth)
        return max(l_depth, r_depth) + 1
