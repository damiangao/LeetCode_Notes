class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        return dfs(root, 0);
    }

    int dfs(TreeNode* root, int curr){
        if(root == nullptr) return -1;
        curr = curr*2+root->val;
        int l = dfs(root->left, curr);
        int r = dfs(root->right, curr);
        if(l == -1 && r ==-1) return curr;
        if(l == -1) return r;
        if(r == -1) return l;
        return l + r;
    }
};
