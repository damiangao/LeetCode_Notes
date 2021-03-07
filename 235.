class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> ps, qs;

        dfs(root, p, ps);
        dfs(root, q, qs);

        TreeNode* res = root;

        int len = min(ps.size(), qs.size());
        for(int i = 0; i < len; i++){
            if(ps[i] != qs[i]) break;
            res = ps[i];
        }
        return res;
    }

    bool dfs(TreeNode* root, TreeNode* t, vector<TreeNode*> & path){
        if(root == nullptr) return false;
        
        path.push_back(root);
        
        if(root == t) return true;

        bool l = dfs(root->left, t, path);
        bool r = dfs(root->right, t, path);

        if(!l && !r){
            path.pop_back();
            return false;
        }

        return true;
    }
};
