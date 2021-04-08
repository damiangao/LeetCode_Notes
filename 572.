//DFS
class Solution {
public:
    queue<TreeNode*> q;

    bool isSubtree(TreeNode* s, TreeNode* t) {
        q.push(s);
        while(!q.empty()){
            TreeNode* curr = q.front();
            if(sameTree(curr, t))
                return true;
            if(curr->left)
                q.push(curr->left);
            if(curr->right)
                q.push(curr->right);
            q.pop(); 
        }
        return false;
    }

    bool sameTree(TreeNode* s, TreeNode* t){
        if(s==nullptr && t==nullptr)
            return true;
        if(s==nullptr || t==nullptr)
            return false;
        if(s->val == t->val)
            return sameTree(s->left, t->left) & sameTree(s->right, t->right);
        return false;
    }
};

# python
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s:
            return False

        return self.isSametree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSametree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        
        return s.val == t.val and self.isSametree(s.left, t.left) and self.isSametree(s.right, t.right)
