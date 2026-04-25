class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        if(root == nullptr) return true;
        return dfs(root, root->val);
    }

    bool dfs(TreeNode* root, int val){
        if(root == nullptr) return true;
        if(root->val == val) return dfs(root->left, val) && dfs(root->right, val);
        return false;
    }
};
