class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return dfs(nums, 0, nums.size()-1);
    }

    TreeNode* dfs(vector<int>& nums, int l, int r){
        if(l > r) return nullptr;

        int mid = (l+r) >> 1;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = dfs(nums, l, mid-1);
        root->right = dfs(nums, mid+1, r);
        return root;
    }
};
