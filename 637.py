# bad solution
class Solution {
public:
    queue<TreeNode*> curr_level;
    vector<double> res;
    vector<double> averageOfLevels(TreeNode* root) {
        queue<TreeNode*> curr_level;
        curr_level.push(root);
        while(!curr_level.empty()){
            double ans = 0;
            int count = 0;
            queue<TreeNode*> next_level;
            while(!curr_level.empty()){
                TreeNode* curr = curr_level.front();
                ans += curr->val;
                if(curr->left != nullptr)
                    next_level.push(curr->left);
                if(curr->right != nullptr)
                    next_level.push(curr->right);
                curr_level.pop();
                count++;
            }
            res.push_back(ans/count);
            curr_level = next_level;
        }
        return res;
    }
};
