# naive solution
class Solution {
public:
    vector<int> read;
    vector<int> findMode(TreeNode* root) {
        vector<int> res;
        bfs(root);
        unordered_map<int, int> mp;
        int max_count = 0;
        for(auto x : read)
            mp[x]++;
        for(auto x : mp){
            if(x.second > max_count)
                max_count = x.second;
        }
        for(auto x : mp){
            if(x.second == max_count){
                res.push_back(x.first);
            }
        }
        return res;
    }

    void bfs(TreeNode* root){
        if(root == nullptr) return;
        read.push_back(root->val);
        bfs(root->left);
        bfs(root->right);
    }
};
