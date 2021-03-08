class Solution {
public:
    vector<int> res;
    vector<int> postorder(Node* root) {
        dfs(root);
        return res;
    }

    void dfs(Node* root){
        if(root == nullptr) return;
        for(auto x : root->children)
            dfs(x);
        res.push_back(root->val);
    }
};
