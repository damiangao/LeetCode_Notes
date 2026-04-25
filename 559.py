class Solution {
public:
    int maxDepth(Node* root) {
        if(root == nullptr) return 0;
        int res = 0;
        int t = 0;
        for(auto x : root->children){
            t = maxDepth(x);
            if(t > res) res = t;
        }
        return res + 1;
    }
};
