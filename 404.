class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(root==NULL)
            return 0;

        int res = 0;

        if(root->left!=NULL && root->left->left==NULL && root->left->right==NULL)
            res = root->left->val; // 有左叶子
        
        return  res + sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    }
};
