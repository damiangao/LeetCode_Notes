class Solution {
public:
    int findSecondMinimumValue(TreeNode *root) {
        if (root->left == nullptr)
            return -1;

        int parent = root->val;
        int left = root->left->val, right = root->right->val;

        if (left == parent)
            left = findSecondMinimumValue(root->left);
        if (right == parent)
            right = findSecondMinimumValue(root->right);

        if (left == parent && right == parent)
            return -1;

        if (left == -1)
            return right;
        else if (right == -1)
            return left;
        else
            return left > right ? right : left;
    }
};
