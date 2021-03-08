class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(root == nullptr) return true;
        queue<TreeNode*> l, r;
        l.push(root->left);
        r.push(root->right);

        while(!l.empty() && !r.empty()){
            TreeNode* l_c = l.front();
            TreeNode* r_c = r.front();
            if(!isEq(l_c, r_c)) return false;
            l.pop();
            r.pop();
            if(l_c == nullptr && r_c==nullptr) continue;
            l.push(l_c->left);
            l.push(l_c->right);
            r.push(r_c->right);
            r.push(r_c->left);
        }

        if(l.empty() && r.empty()) return true;
        return false;
    }

    bool isEq(TreeNode* p, TreeNode* q){
        if(p == nullptr && q == nullptr)
            return true;
        if(p == nullptr || q == nullptr)
            return false;
        
        return p->val == q->val;
    }
};
