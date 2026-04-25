class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(root==nullptr)
            return 0;
        int val = root->val;

        if(val < low)
            return rangeSumBST(root->right, low, high);
        if(val > high)
            return rangeSumBST(root->left, low, high);
        
        return val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
    }
};
