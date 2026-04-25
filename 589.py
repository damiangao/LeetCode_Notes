//recursion
class Solution {
public:
    vector<int> res;
    vector<int> preorder(Node* root) {
        dfs(root);
        return res;
    }
    void dfs(Node* root){
        if(root == nullptr) return;
        res.push_back(root->val);
        for(auto x : root->children)
            dfs(x);
    }
};

//iteration
class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> res;
        stack<Node*> stk;
        stk.push(root);
        Node* curr = root;
        while(!stk.empty()){
            curr = stk.top();
            stk.pop();
            if(curr == nullptr) continue;
            res.push_back(curr->val);
            for(int i=(curr->children).size()-1;i>=0;i--){
                stk.push((curr->children)[i]);
            }
        }
        return res;
    }
};
