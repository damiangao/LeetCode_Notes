class Solution {
public:
    queue<TreeNode*> q;
    TreeNode* increasingBST(TreeNode* root) {
        dfs(root);
        if(q.empty()) return root;
        TreeNode* head = new TreeNode(0);
        TreeNode* curr = head;
        while(!q.empty()){
            curr->right = q.front();
            q.pop();
            curr = curr->right;
        }
        return head->right;
    }

    void dfs(TreeNode* root){
        if(root == nullptr) return;
        dfs(root->left);
        root->left = nullptr;
        q.push(root);
        dfs(root->right);
    }
};
