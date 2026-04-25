class Solution {
public:
    bool isValidSerialization(string preorder) {
        int n = preorder.size();
        if (n == 0) return true;
        stack<int> stk;
        stk.push(1);
        int i = 0;
        while (i < n) {
            if (stk.empty()) return false;
            stk.top();
            char curr = preorder[i];
            if (curr == ',') i++;
            else {
                while (i < n && preorder[i] != ',') {
                    i++;
                }
                stk.top()--;
                if (stk.top() == 0)
                    stk.pop();
                if (curr != '#')
                    stk.push(2);
            }
        }
        return stk.empty();
    }
};
